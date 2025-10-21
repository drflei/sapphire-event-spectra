#!/bin/bash
# Installation script for sapphire-event-spectra package

echo "=================================================="
echo "SAPPHIRE Event Spectra - Installation Script"
echo "=================================================="
echo ""

# Check if we're in the right directory
if [ ! -f "setup.py" ]; then
    echo "❌ Error: setup.py not found. Please run this script from the sapphire-event-spectra directory."
    exit 1
fi

echo "Choose installation method:"
echo "1) Install in development mode (recommended for development)"
echo "2) Regular installation"
echo "3) Create and use virtual environment (recommended)"
echo ""
read -p "Enter choice [1-3]: " choice

case $choice in
    1)
        echo ""
        echo "Installing in development mode..."
        pip install -e . || {
            echo "❌ Installation failed. Try option 3 (virtual environment) instead."
            exit 1
        }
        ;;
    2)
        echo ""
        echo "Installing package..."
        pip install . || {
            echo "❌ Installation failed. Try option 3 (virtual environment) instead."
            exit 1
        }
        ;;
    3)
        echo ""
        echo "Creating virtual environment..."
        python3 -m venv venv
        echo "Activating virtual environment..."
        source venv/bin/activate
        echo "Upgrading pip..."
        pip install --upgrade pip
        echo "Installing package in development mode..."
        pip install -e .
        echo ""
        echo "✅ Installation complete!"
        echo ""
        echo "To use the package:"
        echo "  1. Activate the virtual environment:"
        echo "     source venv/bin/activate"
        echo "  2. Run Python or Jupyter:"
        echo "     python test_package.py"
        echo "     jupyter notebook examples.ipynb"
        echo "  3. To deactivate:"
        echo "     deactivate"
        exit 0
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "✅ Installation complete!"
echo ""
echo "To test the installation, run:"
echo "  python test_package.py"
echo ""
echo "To see usage examples, open:"
echo "  jupyter notebook examples.ipynb"
