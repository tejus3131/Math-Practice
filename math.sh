#!/bin/sh

ALIAS_CMD="sh -c \"\$(curl -fsSL https://raw.githubusercontent.com/tejus3131/Math-Practice/refs/heads/master/math.sh)\""

# Detect OS and Shell
OS="$(uname -s)"
SHELL_NAME="$(basename $SHELL)"

echo "Detected OS: $OS"
echo "Detected Shell: $SHELL_NAME"

# Define the alias for the correct shell config file
if [ "$SHELL_NAME" = "bash" ]; then
    echo "alias math=\"$ALIAS_CMD\"" >> ~/.bashrc
    source ~/.bashrc
elif [ "$SHELL_NAME" = "zsh" ]; then
    echo "alias math=\"$ALIAS_CMD\"" >> ~/.zshrc
    source ~/.zshrc
elif [ "$SHELL_NAME" = "fish" ]; then
    echo "alias math \"$ALIAS_CMD\"" >> ~/.config/fish/config.fish
    source ~/.config/fish/config.fish
elif [ "$OS" = "Darwin" ] && [ "$SHELL_NAME" = "sh" ]; then  # macOS default shell
    echo "alias math=\"$ALIAS_CMD\"" >> ~/.bash_profile
    source ~/.bash_profile
elif [ "$OS" = "Linux" ] && [ "$SHELL_NAME" = "sh" ]; then  # Linux default shell
    echo "alias math=\"$ALIAS_CMD\"" >> ~/.profile
    source ~/.profile
else
    echo "Unsupported shell. You can manually set alias math=\"$ALIAS_CMD\" in your shell config."
fi

echo "Alias 'math' set successfully! 🎉"
echo "You can now run: math"

# ---------------- Python Script Execution ---------------- #

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
