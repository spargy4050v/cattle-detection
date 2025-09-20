# 🐄 Cattle Breed Detection System# Cattle Detection Project



A modern AI-powered web application for identifying Indian cattle breeds using deep learning. Upload or capture images of cattle and get instant breed predictions with confidence scores.This project includes both a web frontend for cattle breed identification and a FastAPI backend with AI model integration.



![Cattle Detection Demo](https://img.shields.io/badge/AI-Cattle%20Detection-green) ![Python](https://img.shields.io/badge/Python-3.8+-blue) ![TensorFlow](https://img.shields.io/badge/TensorFlow-2.20.0-orange) ![FastAPI](https://img.shields.io/badge/FastAPI-0.116.2-teal)## 📁 Project Structure



## 🎯 Features```

cattle-detection/

- **🔍 AI-Powered Detection**: Identifies 12 Indian cattle breeds with high accuracy├── index.html              # Web frontend interface

- **📸 Multiple Input Methods**: Upload images or use live camera capture├── script.js               # Frontend JavaScript logic

- **⚡ Real-time Predictions**: Fast inference with confidence scores├── style.css               # Frontend styling

- **🌐 Web Interface**: Clean, responsive frontend with Tailwind CSS├── README.md               # This file

- **🚀 REST API**: FastAPI backend for easy integration└── api/                    # Backend API directory

- **📱 Mobile Friendly**: Works on desktop and mobile devices    ├── main.py             # FastAPI application

    ├── requirements.txt    # Python dependencies

## 🐮 Supported Cattle Breeds    ├── start.bat          # Windows startup script

    ├── test_api.py        # API testing script

1. **Dangi** - Draft breed from Maharashtra    └── models/

2. **Gir** - Famous dairy breed from Gujarat        ├── indian_cattle_model.h5    # Your trained model (place here)

3. **Hallikar** - Draught breed from Karnataka        └── class_labels.json         # Breed class labels

4. **Hariana** - Dual-purpose breed from Haryana```

5. **Kangayam** - Draught breed from Tamil Nadu

6. **Kankrej** - Dual-purpose breed from Gujarat/Rajasthan## 🚀 Quick Start

7. **Khillari** - Draught breed from Maharashtra

8. **Ongole** - Large dairy breed from Andhra Pradesh### 1. Frontend (Web Interface)

9. **Rathi** - Dual-purpose breed from RajasthanSimply open `index.html` in a web browser to use the basic web interface.

10. **Red Sindhi** - Dairy breed originally from Sindh

11. **Sahiwal** - High-yielding dairy breed from Punjab### 2. Backend API Setup

12. **Tharparkar** - Dual-purpose breed from Rajasthan

Navigate to the API directory:

## 🛠️ Technology Stack```bash

cd api

### Backend```

- **Python 3.8+** - Core programming language

- **TensorFlow 2.20.0** - Deep learning frameworkInstall Python dependencies:

- **FastAPI 0.116.2** - Modern web framework for APIs```bash

- **Uvicorn** - ASGI server for FastAPIpython -m venv venv

- **Pillow** - Image processing libraryvenv\Scripts\activate  # Windows

- **NumPy** - Numerical computingpip install -r requirements.txt

```

### Frontend

- **HTML5** - Markup structure**Place your model:**

- **JavaScript (ES6+)** - Interactive functionality- Copy your `indian_cattle_model.h5` file to `api/models/`

- **Tailwind CSS** - Utility-first styling

- **Fetch API** - HTTP requests to backend**Start the API server:**

```bash

### Modelpython main.py

- **Convolutional Neural Network** - Deep learning architecture```

- **TensorFlow/Keras** - Model training and inference

- **H5 Format** - Model serialization (36MB optimized model)The API will be available at: `http://127.0.0.1:8000`



## 📋 Prerequisites### 3. Integration Testing



Before you begin, ensure you have the following installed:1. Start the API server (step 2)

2. Open the web frontend (`index.html`)

- **Python 3.8 or higher** ([Download Python](https://python.org/downloads/))3. The frontend will automatically connect to the API for real predictions!

- **Git** ([Download Git](https://git-scm.com/downloads))

- **Modern web browser** (Chrome, Firefox, Safari, Edge)## 🔗 API Endpoints



## 🚀 Quick Start- `GET /` - Health check

- `GET /health` - Detailed status

### 1. Clone the Repository- `POST /predict_breed` - Main prediction endpoint

- `POST /predict` - Alternative endpoint

```bash

# Clone the project## 🎯 Supported Breeds

git clone https://github.com/your-username/cattle-detection.git

The model identifies these 12 Indian cattle breeds:

# Navigate to project directory1. Dangi

cd cattle-detection2. Gir

```3. Hallikar

4. Hariana

### 2. Automatic Setup (Recommended)5. Kangayam

6. Kankrej

For Windows users, use the automated setup script:7. Khillari

8. Ongole

```bash9. Rathi

# Navigate to API directory10. Red_Sindhi

cd api11. Sahiwal

12. Tharparkar

# Run the setup script (creates venv, installs dependencies, starts server)

start.bat## 🛠️ Development

```

### Frontend Features:

The script will:- Upload or camera capture

- ✅ Create Python virtual environment- Image preview

- ✅ Install all required dependencies- Real-time AI predictions

- ✅ Start the FastAPI server- Results display with confidence scores

- ✅ Open API at `http://127.0.0.1:8000`

### Backend Features:

### 3. Manual Setup (Alternative)- FastAPI with automatic documentation

- TensorFlow model integration

If you prefer manual setup or are on Linux/Mac:- Image preprocessing

- CORS enabled for web frontend

```bash- Health monitoring and logging

# Create virtual environment

python -m venv venv## 📊 Usage



# Activate virtual environment1. **Web Interface:** Open `index.html` in browser

# On Windows:2. **Upload/Capture:** Select cattle image

venv\Scripts\activate3. **Predict:** Click predict button

# On Linux/Mac:4. **Results:** View breed identification with confidence

source venv/bin/activate

The system automatically uses the AI API when available, with graceful fallback to simulation mode.

# Navigate to API directory

cd api## 🔧 Troubleshooting



# Install dependencies**API not connecting:**

pip install -r requirements.txt- Ensure API server is running on port 8000

- Check if model file is placed correctly in `api/models/`

# Start the server

python main.py**Model loading issues:**

```- Verify TensorFlow version compatibility

- Ensure sufficient RAM for model loading

### 4. Access the Application

**Web interface issues:**

1. **Backend API**: Open `http://127.0.0.1:8000` in your browser- Use modern browser with JavaScript enabled

2. **API Documentation**: Visit `http://127.0.0.1:8000/docs` for interactive API docs- Allow camera permissions for capture feature
3. **Frontend**: Open `index.html` in your browser for the web interface

## 🖥️ Usage Guide

### Web Interface

1. **Open the Frontend**:
   - Open `index.html` in your web browser
   - Or serve it using a local server for better performance

2. **Upload an Image**:
   - Click "Choose Image" tab
   - Select a cattle image from your device
   - Click "Predict Breed" button

3. **Use Camera Capture**:
   - Click "Use Camera" tab
   - Allow camera permissions
   - Position cattle in frame
   - Click "Capture Photo"
   - Click "Predict Breed" button

4. **View Results**:
   - Get breed prediction with confidence percentage
   - See top 3 most likely breeds
   - Results appear in real-time

### API Usage

The FastAPI backend provides REST endpoints for integration:

#### Health Check
```bash
GET http://127.0.0.1:8000/
# Returns: {"status": "running", "model_loaded": true}
```

#### Predict Breed
```bash
POST http://127.0.0.1:8000/predict_breed
Content-Type: multipart/form-data

# Form data:
file: [cattle_image.jpg]

# Response:
{
  "prediction": "Gir",
  "confidence": 0.9974,
  "filename": "cattle_image.jpg",
  "top_predictions": [
    {"breed": "Gir", "confidence": 0.9974},
    {"breed": "Sahiwal", "confidence": 0.0015},
    {"breed": "Red_Sindhi", "confidence": 0.0008}
  ]
}
```

### Python Integration

```python
import requests

# Predict cattle breed
with open('cattle_photo.jpg', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://127.0.0.1:8000/predict_breed', files=files)
    result = response.json()
    
    print(f"Breed: {result['prediction']}")
    print(f"Confidence: {result['confidence']:.2%}")
```

## 📁 Project Structure

```
cattle-detection/
├── 📄 README.md                    # Project documentation
├── 🚫 .gitignore                   # Git ignore rules
├── 🌐 index.html                   # Web interface
├── ⚡ script.js                    # Frontend JavaScript
├── 🎨 style.css                    # Styling
├── 📁 venv/                        # Virtual environment (auto-created)
└── 📁 api/                         # Backend API
    ├── 🐍 main.py                  # FastAPI server
    ├── 📋 requirements.txt         # Python dependencies
    ├── 🚀 start.bat               # Windows setup script
    └── 📁 models/                  # AI models and data
        ├── 🤖 cattle_detection_final.h5    # Trained model (36MB)
        └── 🏷️ class_labels.json            # Breed labels
```

## 🔧 Configuration

### Model Configuration

The system uses a pre-trained TensorFlow model optimized for cattle breed detection:

- **Input Size**: 224x224x3 (RGB images)
- **Model Size**: 36MB (optimized for deployment)
- **Architecture**: Convolutional Neural Network
- **Output**: 13 classes (12 breeds + background)

### API Configuration

Modify `api/main.py` for custom settings:

```python
# Image processing settings
IMG_SIZE = 224  # Input image size for model

# Server settings (in main.py)
uvicorn.run("main:app", host="127.0.0.1", port=8000)
```

### Frontend Configuration

Update `script.js` for custom API endpoints:

```javascript
// API endpoint for predictions
const API_URL = "http://127.0.0.1:8000/predict_breed";
```

## 🔍 Troubleshooting

### Common Issues

**1. Model Not Loading**
```
Error: Model file not found
Solution: Ensure cattle_detection_final.h5 exists in api/models/
```

**2. Permission Errors on Windows**
```
Error: Cannot access camera
Solution: Allow camera permissions in browser settings
```

**3. Python Import Errors**
```
Error: No module named 'tensorflow'
Solution: Ensure virtual environment is activated and dependencies installed
```

**4. Port Already in Use**
```
Error: Port 8000 is already in use
Solution: Change port in main.py or kill existing process
```

### Performance Tips

1. **First Prediction Slow**: TensorFlow model loading takes time on first request
2. **Memory Usage**: Close other applications if running on low-memory systems
3. **Image Size**: Smaller images (< 5MB) process faster
4. **Browser Cache**: Refresh page if predictions seem cached

### Debug Mode

Enable detailed logging in `main.py`:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Test thoroughly**
5. **Commit changes**: `git commit -m 'Add amazing feature'`
6. **Push to branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

### Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/cattle-detection.git
cd cattle-detection

# Set up development environment
cd api
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

# Run in development mode
python main.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **TensorFlow Team** - For the amazing deep learning framework
- **FastAPI** - For the modern Python web framework
- **Indian Council of Agricultural Research** - For cattle breed documentation
- **Contributors** - Thank you to all contributors who helped improve this project

## 📞 Support

- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/your-username/cattle-detection/issues)
- **Discussions**: Join our [GitHub Discussions](https://github.com/your-username/cattle-detection/discussions)
- **Email**: contact@your-domain.com

## 🔄 Version History

- **v1.0.0** (2025-09-21)
  - ✅ Initial release
  - ✅ 12 cattle breed detection
  - ✅ Web interface with camera support
  - ✅ FastAPI backend
  - ✅ Optimized TensorFlow model

---

**Made with ❤️ for Indian Agriculture and Cattle Farming**

*Last updated: September 21, 2025*