# 🐄 Cattle Breed Detection System# 🐄 Cattle Breed Detection System# Cattle Detection Project



A modern AI-powered web application for identifying Indian cattle breeds using deep learning. Upload or capture images of cattle and get instant breed predictions with confidence scores.



![Cattle Detection Demo](https://img.shields.io/badge/AI-Cattle%20Detection-green) ![Python](https://img.shields.io/badge/Python-3.8+-blue) ![TensorFlow](https://img.shields.io/badge/TensorFlow-2.20.0-orange) ![FastAPI](https://img.shields.io/badge/FastAPI-0.116.2-teal)A modern AI-powered web application for identifying Indian cattle breeds using deep learning. Upload or capture images of cattle and get instant breed predictions with confidence scores.This project includes both a web frontend for cattle breed identification and a FastAPI backend with AI model integration.



## 🚀 Quick Start (3 Simple Steps)



### 1. Clone the Repository![Cattle Detection Demo](https://img.shields.io/badge/AI-Cattle%20Detection-green) ![Python](https://img.shields.io/badge/Python-3.8+-blue) ![TensorFlow](https://img.shields.io/badge/TensorFlow-2.20.0-orange) ![FastAPI](https://img.shields.io/badge/FastAPI-0.116.2-teal)## 📁 Project Structure

```bash

git clone https://github.com/your-username/cattle-detection.git

cd cattle-detection

```## 🎯 Features```



### 2. Setup Backend (Auto-Install Dependencies)cattle-detection/

```bash

# Navigate to API directory- **🔍 AI-Powered Detection**: Identifies 12 Indian cattle breeds with high accuracy├── index.html              # Web frontend interface

cd api

- **📸 Multiple Input Methods**: Upload images or use live camera capture├── script.js               # Frontend JavaScript logic

# Run setup script (installs everything + starts server)

start.bat- **⚡ Real-time Predictions**: Fast inference with confidence scores├── style.css               # Frontend styling

```

**This will:**- **🌐 Web Interface**: Clean, responsive frontend with Tailwind CSS├── README.md               # This file

- ✅ Create Python virtual environment

- ✅ Install TensorFlow, FastAPI, and all dependencies- **🚀 REST API**: FastAPI backend for easy integration└── api/                    # Backend API directory

- ✅ Start the API server on `http://127.0.0.1:8000`

- **📱 Mobile Friendly**: Works on desktop and mobile devices    ├── main.py             # FastAPI application

### 3. Run Frontend with Live Server

**Option A: Using VS Code with Git Extension Pack**    ├── requirements.txt    # Python dependencies

1. Install **"Git Extension Pack"** in VS Code (includes Live Server)

2. Right-click on `index.html`## 🐮 Supported Cattle Breeds    ├── start.bat          # Windows startup script

3. Select **"Open with Live Server"**

4. Frontend opens in browser and connects to backend automatically    ├── test_api.py        # API testing script



**Option B: Simple Browser Method**1. **Dangi** - Draft breed from Maharashtra    └── models/

- Just open `index.html` in your browser (Chrome, Firefox, etc.)

2. **Gir** - Famous dairy breed from Gujarat        ├── indian_cattle_model.h5    # Your trained model (place here)

🎉 **That's it! Your cattle detection system is now running!**

3. **Hallikar** - Draught breed from Karnataka        └── class_labels.json         # Breed class labels

## 🎯 Features

4. **Hariana** - Dual-purpose breed from Haryana```

- **🔍 AI-Powered Detection**: Identifies 12 Indian cattle breeds with high accuracy

- **📸 Multiple Input Methods**: Upload images or use live camera capture5. **Kangayam** - Draught breed from Tamil Nadu

- **⚡ Real-time Predictions**: Fast inference with confidence scores

- **🌐 Web Interface**: Clean, responsive frontend with Tailwind CSS6. **Kankrej** - Dual-purpose breed from Gujarat/Rajasthan## 🚀 Quick Start

- **🚀 REST API**: FastAPI backend for easy integration

- **📱 Mobile Friendly**: Works on desktop and mobile devices7. **Khillari** - Draught breed from Maharashtra



## 🐮 Supported Cattle Breeds8. **Ongole** - Large dairy breed from Andhra Pradesh### 1. Frontend (Web Interface)



1. **Dangi** - Draft breed from Maharashtra9. **Rathi** - Dual-purpose breed from RajasthanSimply open `index.html` in a web browser to use the basic web interface.

2. **Gir** - Famous dairy breed from Gujarat

3. **Hallikar** - Draught breed from Karnataka10. **Red Sindhi** - Dairy breed originally from Sindh

4. **Hariana** - Dual-purpose breed from Haryana

5. **Kangayam** - Draught breed from Tamil Nadu11. **Sahiwal** - High-yielding dairy breed from Punjab### 2. Backend API Setup

6. **Kankrej** - Dual-purpose breed from Gujarat/Rajasthan

7. **Khillari** - Draught breed from Maharashtra12. **Tharparkar** - Dual-purpose breed from Rajasthan

8. **Ongole** - Large dairy breed from Andhra Pradesh

9. **Rathi** - Dual-purpose breed from RajasthanNavigate to the API directory:

10. **Red Sindhi** - Dairy breed originally from Sindh

11. **Sahiwal** - High-yielding dairy breed from Punjab## 🛠️ Technology Stack```bash

12. **Tharparkar** - Dual-purpose breed from Rajasthan

cd api

## 🛠️ Technology Stack

### Backend```

### Backend

- **Python 3.8+** - Core programming language- **Python 3.8+** - Core programming language

- **TensorFlow 2.20.0** - Deep learning framework

- **FastAPI 0.116.2** - Modern web framework for APIs- **TensorFlow 2.20.0** - Deep learning frameworkInstall Python dependencies:

- **Uvicorn** - ASGI server for FastAPI

- **Pillow** - Image processing library- **FastAPI 0.116.2** - Modern web framework for APIs```bash

- **NumPy** - Numerical computing

- **Uvicorn** - ASGI server for FastAPIpython -m venv venv

### Frontend

- **HTML5** - Markup structure- **Pillow** - Image processing libraryvenv\Scripts\activate  # Windows

- **JavaScript (ES6+)** - Interactive functionality

- **Tailwind CSS** - Utility-first styling- **NumPy** - Numerical computingpip install -r requirements.txt

- **Fetch API** - HTTP requests to backend

```

### Model

- **Convolutional Neural Network** - Deep learning architecture### Frontend

- **TensorFlow/Keras** - Model training and inference

- **H5 Format** - Model serialization (36MB optimized model)- **HTML5** - Markup structure**Place your model:**



## 📋 Prerequisites- **JavaScript (ES6+)** - Interactive functionality- Copy your `indian_cattle_model.h5` file to `api/models/`



Before you begin, ensure you have the following installed:- **Tailwind CSS** - Utility-first styling



- **Python 3.8 or higher** ([Download Python](https://python.org/downloads/))- **Fetch API** - HTTP requests to backend**Start the API server:**

- **Git** ([Download Git](https://git-scm.com/downloads))

- **VS Code** (Optional, for Live Server) ([Download VS Code](https://code.visualstudio.com/))```bash

- **Modern web browser** (Chrome, Firefox, Safari, Edge)

### Modelpython main.py

## 🖥️ Usage Guide

- **Convolutional Neural Network** - Deep learning architecture```

### Web Interface

- **TensorFlow/Keras** - Model training and inference

1. **Upload an Image**:

   - Click "Choose Image" tab- **H5 Format** - Model serialization (36MB optimized model)The API will be available at: `http://127.0.0.1:8000`

   - Select a cattle image from your device

   - Click "Predict Breed" button



2. **Use Camera Capture**:## 📋 Prerequisites### 3. Integration Testing

   - Click "Use Camera" tab

   - Allow camera permissions

   - Position cattle in frame

   - Click "Capture Photo"Before you begin, ensure you have the following installed:1. Start the API server (step 2)

   - Click "Predict Breed" button

2. Open the web frontend (`index.html`)

3. **View Results**:

   - Get breed prediction with confidence percentage- **Python 3.8 or higher** ([Download Python](https://python.org/downloads/))3. The frontend will automatically connect to the API for real predictions!

   - See top 3 most likely breeds

   - Results appear in real-time- **Git** ([Download Git](https://git-scm.com/downloads))



### API Usage- **Modern web browser** (Chrome, Firefox, Safari, Edge)## 🔗 API Endpoints



The FastAPI backend provides REST endpoints for integration:



#### Health Check## 🚀 Quick Start- `GET /` - Health check

```bash

GET http://127.0.0.1:8000/- `GET /health` - Detailed status

# Returns: {"status": "running", "model_loaded": true}

```### 1. Clone the Repository- `POST /predict_breed` - Main prediction endpoint



#### Predict Breed- `POST /predict` - Alternative endpoint

```bash

POST http://127.0.0.1:8000/predict_breed```bash

Content-Type: multipart/form-data

# Clone the project## 🎯 Supported Breeds

# Form data:

file: [cattle_image.jpg]git clone https://github.com/your-username/cattle-detection.git



# Response:The model identifies these 12 Indian cattle breeds:

{

  "prediction": "Gir",# Navigate to project directory1. Dangi

  "confidence": 0.9974,

  "filename": "cattle_image.jpg",cd cattle-detection2. Gir

  "top_predictions": [

    {"breed": "Gir", "confidence": 0.9974},```3. Hallikar

    {"breed": "Sahiwal", "confidence": 0.0015},

    {"breed": "Red_Sindhi", "confidence": 0.0008}4. Hariana

  ]

}### 2. Automatic Setup (Recommended)5. Kangayam

```

6. Kankrej

### Python Integration

For Windows users, use the automated setup script:7. Khillari

```python

import requests8. Ongole



# Predict cattle breed```bash9. Rathi

with open('cattle_photo.jpg', 'rb') as f:

    files = {'file': f}# Navigate to API directory10. Red_Sindhi

    response = requests.post('http://127.0.0.1:8000/predict_breed', files=files)

    result = response.json()cd api11. Sahiwal

    

    print(f"Breed: {result['prediction']}")12. Tharparkar

    print(f"Confidence: {result['confidence']:.2%}")

```# Run the setup script (creates venv, installs dependencies, starts server)



## 📁 Project Structurestart.bat## 🛠️ Development



``````

cattle-detection/

├── 📄 README.md                    # Project documentation### Frontend Features:

├── 🚫 .gitignore                   # Git ignore rules

├── 🌐 index.html                   # Web interfaceThe script will:- Upload or camera capture

├── ⚡ script.js                    # Frontend JavaScript

├── 🎨 style.css                    # Styling- ✅ Create Python virtual environment- Image preview

├── 📁 venv/                        # Virtual environment (auto-created)

└── 📁 api/                         # Backend API- ✅ Install all required dependencies- Real-time AI predictions

    ├── 🐍 main.py                  # FastAPI server

    ├── 📋 requirements.txt         # Python dependencies- ✅ Start the FastAPI server- Results display with confidence scores

    ├── 🚀 start.bat               # Windows setup script

    └── 📁 models/                  # AI models and data- ✅ Open API at `http://127.0.0.1:8000`

        ├── 🤖 cattle_detection_final.h5    # Trained model (36MB)

        └── 🏷️ class_labels.json            # Breed labels### Backend Features:

```

### 3. Manual Setup (Alternative)- FastAPI with automatic documentation

## 🔧 Alternative Setup Methods

- TensorFlow model integration

### Manual Setup (Advanced Users)

If you prefer manual setup or are on Linux/Mac:- Image preprocessing

If you prefer manual setup or are on Linux/Mac:

- CORS enabled for web frontend

```bash

# Create virtual environment```bash- Health monitoring and logging

python -m venv venv

# Create virtual environment

# Activate virtual environment

# On Windows:python -m venv venv## 📊 Usage

venv\Scripts\activate

# On Linux/Mac:

source venv/bin/activate

# Activate virtual environment1. **Web Interface:** Open `index.html` in browser

# Navigate to API directory

cd api# On Windows:2. **Upload/Capture:** Select cattle image



# Install dependenciesvenv\Scripts\activate3. **Predict:** Click predict button

pip install -r requirements.txt

# On Linux/Mac:4. **Results:** View breed identification with confidence

# Start the server

python main.pysource venv/bin/activate

```

The system automatically uses the AI API when available, with graceful fallback to simulation mode.

### Running Without Live Server

# Navigate to API directory

If you don't want to use Live Server:

cd api## 🔧 Troubleshooting

1. Start the backend: `cd api && start.bat`

2. Open `index.html` directly in any browser

3. The app will work the same way

# Install dependencies**API not connecting:**

## 🔍 Troubleshooting

pip install -r requirements.txt- Ensure API server is running on port 8000

### Common Issues

- Check if model file is placed correctly in `api/models/`

**1. Model Not Loading**

```# Start the server

Error: Model file not found

Solution: Ensure cattle_detection_final.h5 exists in api/models/python main.py**Model loading issues:**

```

```- Verify TensorFlow version compatibility

**2. Cannot Access Camera**

```- Ensure sufficient RAM for model loading

Error: Camera permission denied

Solution: Allow camera permissions in browser settings### 4. Access the Application

```

**Web interface issues:**

**3. Python Import Errors**

```1. **Backend API**: Open `http://127.0.0.1:8000` in your browser- Use modern browser with JavaScript enabled

Error: No module named 'tensorflow'

Solution: Ensure virtual environment is activated and run start.bat2. **API Documentation**: Visit `http://127.0.0.1:8000/docs` for interactive API docs- Allow camera permissions for capture feature

```3. **Frontend**: Open `index.html` in your browser for the web interface



**4. Port Already in Use**## 🖥️ Usage Guide

```

Error: Port 8000 is already in use### Web Interface

Solution: Close other applications using port 8000 or change port in main.py

```1. **Open the Frontend**:

   - Open `index.html` in your web browser

**5. Live Server Not Working**   - Or serve it using a local server for better performance

```

Error: Live Server extension not found2. **Upload an Image**:

Solution: Install Git Extension Pack in VS Code extensions   - Click "Choose Image" tab

```   - Select a cattle image from your device

   - Click "Predict Breed" button

### Performance Tips

3. **Use Camera Capture**:

1. **First Prediction Slow**: TensorFlow model loading takes time on first request   - Click "Use Camera" tab

2. **Memory Usage**: Close other applications if running on low-memory systems   - Allow camera permissions

3. **Image Size**: Smaller images (< 5MB) process faster   - Position cattle in frame

4. **Browser Cache**: Refresh page if predictions seem cached   - Click "Capture Photo"

   - Click "Predict Breed" button

## 🎬 Demo

4. **View Results**:

### Expected Output   - Get breed prediction with confidence percentage

When you upload a cattle image, you'll get results like:   - See top 3 most likely breeds

   - Results appear in real-time

```

Prediction: Gir### API Usage

Confidence: 99.74%

The FastAPI backend provides REST endpoints for integration:

Top 3 Predictions:

1. Gir - 99.74%#### Health Check

2. Sahiwal - 0.15%```bash

3. Red_Sindhi - 0.08%GET http://127.0.0.1:8000/

```# Returns: {"status": "running", "model_loaded": true}

```

## 🤝 Contributing

#### Predict Breed

We welcome contributions! Here's how to get started:```bash

POST http://127.0.0.1:8000/predict_breed

1. **Fork the repository**Content-Type: multipart/form-data

2. **Create a feature branch**: `git checkout -b feature/amazing-feature`

3. **Make your changes**# Form data:

4. **Test thoroughly**file: [cattle_image.jpg]

5. **Commit changes**: `git commit -m 'Add amazing feature'`

6. **Push to branch**: `git push origin feature/amazing-feature`# Response:

7. **Open a Pull Request**{

  "prediction": "Gir",

## 📄 License  "confidence": 0.9974,

  "filename": "cattle_image.jpg",

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  "top_predictions": [

    {"breed": "Gir", "confidence": 0.9974},

## 🙏 Acknowledgments    {"breed": "Sahiwal", "confidence": 0.0015},

    {"breed": "Red_Sindhi", "confidence": 0.0008}

- **TensorFlow Team** - For the amazing deep learning framework  ]

- **FastAPI** - For the modern Python web framework}

- **Indian Council of Agricultural Research** - For cattle breed documentation```

- **Contributors** - Thank you to all contributors who helped improve this project

### Python Integration

## 📞 Support

```python

- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/your-username/cattle-detection/issues)import requests

- **Email**: contact@your-domain.com

# Predict cattle breed

## 🔄 Version Historywith open('cattle_photo.jpg', 'rb') as f:

    files = {'file': f}

- **v1.0.0** (2025-09-21)    response = requests.post('http://127.0.0.1:8000/predict_breed', files=files)

  - ✅ Initial release    result = response.json()

  - ✅ 12 cattle breed detection    

  - ✅ Web interface with camera support    print(f"Breed: {result['prediction']}")

  - ✅ FastAPI backend    print(f"Confidence: {result['confidence']:.2%}")

  - ✅ Optimized TensorFlow model```



---## 📁 Project Structure



**Made with ❤️ for Indian Agriculture and Cattle Farming**```

cattle-detection/

*Last updated: September 21, 2025*├── 📄 README.md                    # Project documentation
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