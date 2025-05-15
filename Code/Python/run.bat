@echo off
REM Install requirements first
echo Installing dependencies...
python -m pip install -r requirements.txt

REM Run the main Python project script
echo Running the project...
python run_project.py

pause
