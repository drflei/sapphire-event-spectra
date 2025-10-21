# SAPPHIRE Event Spectra Package - Quick Start Guide

## 📦 Package Created Successfully!

The `sapphire-event-spectra` package has been created with a complete, professional structure.

## 📁 Package Structure

```
sapphire-event-spectra/
├── sapphire_event_spectra/     # Main package directory
│   ├── __init__.py             # Package initialization
│   ├── core.py                 # Band function & conversions
│   ├── spectra.py              # Spectra generation
│   └── plotting.py             # Visualization utilities
├── setup.py                     # Installation script
├── requirements.txt             # Dependencies
├── README.md                    # Full documentation
├── LICENSE                      # MIT License
├── install.sh                   # Installation helper script
├── demo.py                      # Quick demo (no install needed)
├── test_package.py             # Test suite
└── examples.ipynb              # Usage examples notebook
```

## 🚀 Quick Start

### Option 1: Run Demo Without Installation

```bash
cd sapphire-event-spectra
python demo.py
```

This will:
- ✅ Generate spectra for 3 SAPPHIRE events
- ✅ Create 3 PNG plots
- ✅ Show all package features

### Option 2: Install the Package

#### Using Virtual Environment (Recommended)

```bash
cd sapphire-event-spectra
./install.sh
# Choose option 3 (virtual environment)
```

Then activate and use:

```bash
source venv/bin/activate
python test_package.py    # Run tests
python demo.py            # Run demo
jupyter notebook examples.ipynb  # See examples
```

#### Manual Installation

```bash
cd sapphire-event-spectra

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install package
pip install -e .
```

## 💻 Basic Usage

### In Python Scripts

```python
import sapphire_event_spectra as ses

# Generate spectra
spectra = ses.generate_sapphire_spectra(
    events=['1-in-100-year', '1-in-1000-year']
)

# Access data
data = spectra['1-in-100-year']
energy = data['energy_MeV']
fluence = data['fluence_dJ_dE']  # particles/cm²/sr/MeV

# Plot
ses.plot_spectra_energy(spectra)
```

### In Jupyter Notebooks

See `examples.ipynb` for detailed examples including:
- Generating all or specific events
- Accessing spectrum data
- Energy-rigidity conversions
- Creating custom plots
- Parameter retrieval
- Direct Band function calculations

## 📊 Available Data

Each generated spectrum includes:

**Arrays:**
- `energy_MeV`: Energy grid (MeV)
- `rigidity_GV`: Rigidity grid (GV)
- `fluence_dJ_dR`: Event fluence in rigidity space (particles/cm²/sr/GV)
- `fluence_dJ_dE`: Event fluence in energy space (particles/cm²/sr/MeV)
- `flux_dJ_dR`: Peak flux in rigidity space (particles/cm²/sr/s/GV)
- `flux_dJ_dE`: Peak flux in energy space (particles/cm²/sr/s/MeV)

**Parameters:**
- Band function parameters (ga, gb, R0, C, Rb) for both fluence and flux

## 🎯 Key Features

### ✅ Core Functions
- `band_function_jiggins()` - SAPPHIRE Band function
- `energy_to_rigidity_proton()` - E → R conversion
- `rigidity_to_energy_proton()` - R → E conversion
- `convert_dJ_dR_to_dJ_dE()` - Spectrum conversion

### ✅ Spectra Generation
- `generate_sapphire_spectra()` - Generate event spectra
- `get_sapphire_parameters()` - Get Table 8 parameters
- `SAPPHIRE_EVENTS` - List of available events

### ✅ Plotting
- `plot_spectra_energy()` - Plot in energy space
- `plot_spectra_rigidity()` - Plot in rigidity space
- `plot_both_spaces()` - Plot both together

## 📖 Available Events

1. 1-in-10-year
2. 1-in-20-year
3. 1-in-50-year
4. 1-in-100-year
5. 1-in-300-year
6. 1-in-1000-year
7. 1-in-10000-year

## 🧪 Testing

Run the test suite:

```bash
python test_package.py
```

This verifies:
- ✅ Package imports correctly
- ✅ All functions are available
- ✅ Energy-rigidity conversions work
- ✅ Parameters load correctly
- ✅ Spectra generation succeeds

## 📚 Documentation

- **README.md**: Complete package documentation
- **examples.ipynb**: 10+ usage examples
- **demo.py**: Quick demonstration script
- **Docstrings**: All functions have detailed docstrings

## 🔬 Scientific Reference

Based on:
> Jiggens, P., et al. (2018). "Updated Model of the Solar Energetic Proton 
> Environment in Space." *J. Space Weather Space Clim.*, **8**, A31.
> https://doi.org/10.1051/swsc/2018010

## 🎨 Example Outputs

Running `demo.py` generates:
- `sapphire_energy_space.png` - Fluence & flux vs energy
- `sapphire_rigidity_space.png` - Fluence & flux vs rigidity
- `sapphire_both_spaces.png` - Combined 2×2 plot

## 📝 License

MIT License - Free to use, modify, and distribute

## 🤝 Integration

To use in other projects:

```python
# Add to your requirements.txt
-e /path/to/sapphire-event-spectra

# Or install directly
pip install /path/to/sapphire-event-spectra
```

## 💡 Tips

1. **Use virtual environments** to avoid dependency conflicts
2. **Check examples.ipynb** for detailed usage patterns
3. **Run demo.py first** to verify everything works
4. **All functions have docstrings** - use `help(ses.function_name)`
5. **Units are always per steradian** - remember to account for solid angle

## 🎉 Success!

Your SAPPHIRE event spectra package is ready to use! 🚀

For questions or issues, refer to:
- README.md (detailed documentation)
- examples.ipynb (usage examples)
- Docstrings in the code (help() function)
