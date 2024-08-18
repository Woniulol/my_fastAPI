#!/bin/bash

echo "Starting the environment setup..."

PYTHON_VERSION=$(python3 --version 2>&1)
REQUIRED_VERSION="Python 3.12.4"

if [[ "$PYTHON_VERSION" != "$REQUIRED_VERSION" ]]; then
    echo "Error: Python 3.12.4 is required. Found: $PYTHON_VERSION"
    exit 1
fi

echo "Correct Python version found: $PYTHON_VERSION"

echo "Creating a virtual environment..."
python3 -m venv .venv

# Activate the virtual environment
echo "Activating the virtual environment..."
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

# Print a completion message
echo ""
echo "Setup is complete. The virtual environment is ready to use."
echo "To activate the environment in the future, run: source .venv/bin/activate"
echo "To deactivate, run: deactivate"

source .venv/bin/activate
# Deactivate the virtual environment
# deactivate
