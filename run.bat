@echo off
echo Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install dependencies. Please ensure Python and pip are installed.
    pause
    exit /b
)

echo.
echo Starting Web Crawler Pro...
echo Open your browser to: http://127.0.0.1:5000
echo.
python app.py
pause
