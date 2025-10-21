# SAPPHIRE Event Spectra

Python package for generating SAPPHIRE (Solar Accumulated and Peak Proton and Heavy Ion Radiation Environment) solar particle event spectra.

## Overview

This package implements the SAPPHIRE model for solar proton event spectra as described in:

> Jiggens, P., et al. (2018). "Updated Model of the Solar Energetic Proton Environment in Space." *J. Space Weather Space Clim.*, **8**, A31. https://doi.org/10.1051/swsc/2018010

The SAPPHIRE model provides differential spectra for both:
- **Event-integrated fluence** (time-integrated flux)
- **Event peak flux**

For various return periods: 1-in-10-year, 1-in-20-year, 1-in-50-year, 1-in-100-year, 1-in-300-year, 1-in-1000-year, and 1-in-10000-year events.

## Features

- **Band Function Implementation**: Accurate implementation of the SAPPHIRE Band function with proper break rigidity handling
- **Dual Representations**: Spectra available in both rigidity space (dJ/dR) and energy space (dJ/dE)
- **Energy-Rigidity Conversion**: Built-in utilities for converting between kinetic energy and magnetic rigidity for protons
- **Flexible API**: Easy-to-use functions for generating spectra for any subset of events
- **Visualization Tools**: Ready-to-use plotting functions for both rigidity and energy space
- **Proper Units**: All outputs include per-steradian normalization (particles/cm²/sr/...)

## Installation

### From source (development mode)

```bash
cd sapphire-event-spectra
pip install -e .
```

### Regular installation

```bash
cd sapphire-event-spectra
pip install .
```

## Quick Start

### Generate spectra

```python
import sapphire_event_spectra as ses

# Generate all SAPPHIRE events
spectra = ses.generate_sapphire_spectra()

# Generate specific events
spectra = ses.generate_sapphire_spectra(
    events=['1-in-100-year', '1-in-1000-year'],
    E_min=1.0,      # MeV
    E_max=1e4,      # MeV
    n_points=200
)

# Access data
event_data = spectra['1-in-100-year']
energy = event_data['energy_MeV']
rigidity = event_data['rigidity_GV']
fluence_dJ_dE = event_data['fluence_dJ_dE']  # particles/cm²/sr/MeV
flux_dJ_dE = event_data['flux_dJ_dE']        # particles/cm²/sr/s/MeV
```

### Plot spectra

```python
import sapphire_event_spectra as ses

# Generate spectra
spectra = ses.generate_sapphire_spectra(
    events=['1-in-10-year', '1-in-100-year', '1-in-1000-year', '1-in-10000-year']
)

# Plot in energy space
ses.plot_spectra_energy(spectra)

# Plot in rigidity space
ses.plot_spectra_rigidity(spectra)

# Plot both spaces together
ses.plot_both_spaces(spectra)
```

### Access parameters

```python
import sapphire_event_spectra as ses

# Get SAPPHIRE parameters from Table 8
df_params, gb_fluence, gb_flux = ses.get_sapphire_parameters()

print(df_params)
print(f"Common gamma_beta for fluence: {gb_fluence}")
print(f"Common gamma_beta for flux: {gb_flux}")

# List available events
print(ses.SAPPHIRE_EVENTS)
```

### Use core functions directly

```python
import numpy as np
import sapphire_event_spectra as ses

# Energy to rigidity conversion
E_MeV = np.array([1.0, 10.0, 100.0, 1000.0])
R_GV = ses.energy_to_rigidity_proton(E_MeV)

# Rigidity to energy conversion
E_back = ses.rigidity_to_energy_proton(R_GV)

# Calculate Band function
R = np.logspace(-2, 2, 100)  # GV
ga, gb, R0, C = 0.48, 5.7, 0.0671, 8.73e10
dJ_dR = ses.band_function_jiggins(R, ga, gb, R0, C)
```

## Package Structure

```
sapphire-event-spectra/
├── sapphire_event_spectra/
│   ├── __init__.py      # Package initialization and exports
│   ├── core.py          # Core Band function and conversions
│   ├── spectra.py       # Spectra generation and parameters
│   └── plotting.py      # Visualization utilities
├── setup.py             # Package installation script
├── README.md            # This file
└── LICENSE              # License information
```

## API Reference

### Core Functions (`core.py`)

- `band_function_jiggins(R, ga, gb, R0, C)`: Calculate SAPPHIRE Band function
- `energy_to_rigidity_proton(E_MeV)`: Convert kinetic energy to rigidity
- `rigidity_to_energy_proton(R_GV)`: Convert rigidity to kinetic energy
- `convert_dJ_dR_to_dJ_dE(dJ_dR, E_MeV)`: Convert dJ/dR to dJ/dE

### Spectra Generation (`spectra.py`)

- `generate_sapphire_spectra(events=None, E_min=0.1, E_max=1e5, n_points=200, include_fluence=True, include_flux=True)`: Generate SAPPHIRE spectra
- `get_sapphire_parameters()`: Get Table 8 parameters
- `SAPPHIRE_EVENTS`: List of available event identifiers

### Plotting (`plotting.py`)

- `plot_spectra_rigidity(spectra_results, events=None, ...)`: Plot in rigidity space
- `plot_spectra_energy(spectra_results, events=None, ...)`: Plot in energy space
- `plot_both_spaces(spectra_results, events=None, ...)`: Plot both spaces

## Units

All spectra are provided with proper per-steradian normalization:

- **Event-integrated fluence**:
  - dJ/dR: particles/cm²/sr/GV
  - dJ/dE: particles/cm²/sr/MeV

- **Event peak flux**:
  - dJ/dR: particles/cm²/sr/s/GV
  - dJ/dE: particles/cm²/sr/s/MeV

## Requirements

- Python >= 3.8
- numpy >= 1.20.0
- pandas >= 1.3.0
- matplotlib >= 3.3.0

## Citation

If you use this package in your research, please cite:

```bibtex
@article{jiggens2018sapphire,
  title={Updated Model of the Solar Energetic Proton Environment in Space},
  author={Jiggens, Piers and others},
  journal={Journal of Space Weather and Space Climate},
  volume={8},
  pages={A31},
  year={2018},
  doi={10.1051/swsc/2018010}
}
```

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Authors

MAIRE-S Team

## Acknowledgments

This implementation is based on the SAPPHIRE model developed by Jiggens et al. (2018).
