@echo off
REM Cattle Breed API Start Script for Windows
REM This script sets up and starts the API server

echo 🐄 Starting Cattle Breed Identifier API...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "..\venv" (
    echo 📦 Creating virtual environment...
    cd ..
    python -m venv venv
    cd api
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call ..\venv\Scripts\activate

REM Install dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt

REM Check if model file exists
if not exist "models\indian_cattle_model.h5" (
    echo ⚠️  WARNING: Model file 'models\indian_cattle_model.h5' not found!
    echo Please place your trained model file in the models\ directory.
    echo The API will start but predictions will fail until the model is available.
    echo.
)

REM Start the server
echo 🚀 Starting API server...
echo API will be available at: http://127.0.0.1:8000
echo API documentation: http://127.0.0.1:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo.

python main.py