import tensorflow as tf
import numpy as np
from PIL import Image
import json
import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
import uvicorn
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -------------------------------
# 1️⃣ Configuration
# -------------------------------
MODEL_PATH = "models/cattle_detection_final.h5"
LABELS_PATH = "models/class_labels.json"
IMG_SIZE = 224

# -------------------------------
# 2️⃣ Load model and labels
# -------------------------------
def load_model_and_labels():
    """Load the trained model and class labels"""
    try:
        logger.info("Loading model and labels...")
        
        # Check if labels file exists
        if not os.path.exists(LABELS_PATH):
            raise FileNotFoundError(f"Labels file not found: {LABELS_PATH}")
        
        # Check if model file exists
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
        
        # Load the model
        logger.info(f"Loading model from: {MODEL_PATH}")
        model = tf.keras.models.load_model(MODEL_PATH, compile=False)
        
        # Test the model with dummy input
        dummy_input = np.random.random((1, IMG_SIZE, IMG_SIZE, 3)).astype(np.float32)
        test_pred = model.predict(dummy_input, verbose=0)
        
        # Recompile the model
        model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        
        logger.info(f"✅ Model loaded successfully!")
        logger.info(f"✅ Model output shape: {test_pred.shape}")
        
        # Load labels
        with open(LABELS_PATH, "r") as f:
            class_labels = json.load(f)
        logger.info(f"✅ Labels loaded: {len(class_labels)} classes")
        logger.info(f"Classes: {class_labels}")
        
        # Final test
        dummy_input = np.random.random((1, IMG_SIZE, IMG_SIZE, 3)).astype(np.float32)
        test_pred = model.predict(dummy_input, verbose=0)
        logger.info(f"✅ Final model test successful!")
        logger.info(f"✅ Model ready for predictions!")
        
        return model, class_labels
    
    except Exception as e:
        logger.error(f"❌ Error loading model/labels: {str(e)}")
        raise

# Load model and labels at startup
try:
    model, class_labels = load_model_and_labels()
    DEMO_MODE = False
    logger.info("✅ Model loaded successfully - Running in PRODUCTION mode")
except Exception as e:
    logger.warning(f"⚠️ Could not load model: {e}")
    logger.info("🔧 Running in DEMO mode with mock predictions")
    model, class_labels = None, [
        "Dangi", "Gir", "Hallikar", "Hariana", "Kangayam", 
        "Kankrej", "Khillari", "Ongole", "Rathi", "Red_Sindhi", 
        "Sahiwal", "Tharparkar"
    ]
    DEMO_MODE = True

# -------------------------------
# 3️⃣ Preprocessing function
# -------------------------------
def preprocess_image(image_bytes: bytes, img_size: int = 224) -> np.ndarray:
    """
    Preprocess image for model prediction
    
    Args:
        image_bytes: Raw image bytes
        img_size: Target image size (default 224)
    
    Returns:
        Preprocessed image array ready for prediction
    """
    try:
        # Open image from bytes
        img = Image.open(BytesIO(image_bytes))
        
        # Convert to RGB if needed
        if img.mode != "RGB":
            img = img.convert("RGB")
        
        # Resize image
        img = img.resize((img_size, img_size))
        
        # Convert to numpy array and normalize
        img_array = np.array(img, dtype=np.float32) / 255.0
        
        # Add batch dimension
        img_array = np.expand_dims(img_array, axis=0)
        
        logger.info(f"Image preprocessed: shape {img_array.shape}")
        return img_array
    
    except Exception as e:
        logger.error(f"Error preprocessing image: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Error processing image: {str(e)}")

# -------------------------------
# 4️⃣ Define FastAPI app
# -------------------------------
app = FastAPI(
    title="Cattle Breed Identifier API",
    description="AI-powered cattle breed identification using deep learning",
    version="1.0.0"
)

# Add CORS middleware to allow frontend connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "Cattle Breed Identifier API",
        "status": "running",
        "mode": "DEMO" if DEMO_MODE else "PRODUCTION",
        "model_loaded": model is not None,
        "classes_available": len(class_labels) if class_labels else 0
    }

@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy" if model is not None else "unhealthy",
        "model_path": MODEL_PATH,
        "labels_path": LABELS_PATH,
        "model_loaded": model is not None,
        "classes": class_labels if class_labels else []
    }

@app.post("/predict_breed")
async def predict_breed(file: UploadFile = File(...)):
    """
    Predict cattle breed from uploaded image
    
    Args:
        file: Uploaded image file
    
    Returns:
        Prediction results with breed name and confidence
    """
    try:
        # Check if model is loaded or demo mode
        if not DEMO_MODE and (model is None or class_labels is None):
            raise HTTPException(
                status_code=503, 
                detail="Model not loaded. Please check server configuration."
            )
        
        # Validate file type
        if not file.content_type.startswith('image/'):
            raise HTTPException(
                status_code=400, 
                detail=f"Invalid file type: {file.content_type}. Please upload an image."
            )
        
        # Read file contents
        contents = await file.read()
        logger.info(f"Processing image: {file.filename}, size: {len(contents)} bytes")
        
        if DEMO_MODE:
            # Demo mode - return mock prediction
            import random
            logger.info("🔧 Running in DEMO mode - generating mock prediction")
            
            # Simulate processing time
            import asyncio
            await asyncio.sleep(1)
            
            # Generate random but consistent prediction based on filename
            random.seed(hash(file.filename or "demo") % 1000)
            pred_class_idx = random.randint(0, len(class_labels) - 1)
            pred_class_name = class_labels[pred_class_idx]
            confidence = random.uniform(0.65, 0.95)
            
            # Generate top 3 predictions
            indices = list(range(len(class_labels)))
            random.shuffle(indices)
            top_3_predictions = [
                {
                    "breed": class_labels[indices[0]],
                    "confidence": confidence
                },
                {
                    "breed": class_labels[indices[1]], 
                    "confidence": confidence * 0.8
                },
                {
                    "breed": class_labels[indices[2]],
                    "confidence": confidence * 0.6
                }
            ]
            
            logger.info(f"🔧 Demo prediction: {pred_class_name} ({confidence:.2%})")
            
            return {
                "prediction": pred_class_name,
                "confidence": confidence,
                "filename": file.filename,
                "top_predictions": top_3_predictions,
                "demo_mode": True,
                "message": "This is a demo prediction. Upload a real model for actual predictions."
            }
        
        # Production mode - use actual model
        # Preprocess image
        img_array = preprocess_image(contents, IMG_SIZE)
        
        # Make prediction
        logger.info("Making prediction...")
        pred_probs = model.predict(img_array, verbose=0)
        
        # Handle model output shape mismatch
        num_model_outputs = pred_probs.shape[1]
        num_labels = len(class_labels)
        
        if num_model_outputs != num_labels:
            logger.warning(f"Model outputs {num_model_outputs} classes but only {num_labels} labels available")
            # Truncate predictions to match available labels
            pred_probs = pred_probs[:, :num_labels]
        
        # Get prediction results
        pred_class_idx = int(np.argmax(pred_probs, axis=1)[0])
        
        # Ensure index is within bounds
        if pred_class_idx >= len(class_labels):
            logger.warning(f"Predicted class index {pred_class_idx} out of range, using last available class")
            pred_class_idx = len(class_labels) - 1
            
        pred_class_name = class_labels[pred_class_idx]
        confidence = float(pred_probs[0][pred_class_idx])
        
        # Get top 3 predictions for additional context
        top_3_indices = np.argsort(pred_probs[0])[-3:][::-1]
        top_3_predictions = []
        
        for idx in top_3_indices:
            if idx < len(class_labels):  # Ensure index is valid
                top_3_predictions.append({
                    "breed": class_labels[idx],
                    "confidence": float(pred_probs[0][idx])
                })
        
        logger.info(f"Prediction complete: {pred_class_name} ({confidence:.2%})")
        
        # Return results in format expected by frontend
        return {
            "prediction": pred_class_name,
            "confidence": confidence,
            "filename": file.filename,
            "top_predictions": top_3_predictions,
            "demo_mode": False,
            "all_probabilities": {
                class_labels[i]: float(prob) 
                for i, prob in enumerate(pred_probs[0])
            }
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    """
    Alternative endpoint name for compatibility
    """
    return await predict_breed(file)

# -------------------------------
# 5️⃣ Run the server
# -------------------------------
if __name__ == "__main__":
    logger.info("Starting Cattle Breed Identifier API server...")
    uvicorn.run(
        "main:app", 
        host="127.0.0.1", 
        port=8000, 
        log_level="info"
    )