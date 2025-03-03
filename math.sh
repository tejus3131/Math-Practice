#!/bin/sh

# Check if Python is installed
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "Python is not installed. Please install Python first." >&2
    exit 1
fi

# Use python3 if available, otherwise fallback to python
PYTHON_CMD=$(command -v python3 || command -v python)

# Check if customtkinter is installed, install if missing
$PYTHON_CMD -c "import customtkinter" 2>/dev/null || {
    echo "Installing customtkinter..."
    $PYTHON_CMD -m pip install customtkinter
}

# Fetch and execute the script from GitHub
echo "Running Python script..."
$PYTHON_CMD -c "import requests; exec(requests.get('https://raw.githubusercontent.com/tejus3131/Math-Practice/refs/heads/master/Math.py').content)"
