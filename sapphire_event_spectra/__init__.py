"""
SAPPHIRE Event Spectra Package

Implementation of the SAPPHIRE (Solar Accumulated and Peak Proton and Heavy Ion 
Radiation Environment) model for solar particle event spectra.

Based on:
Jiggens, P., et al. (2018). "Updated Model of the Solar Energetic Proton 
Environment in Space." J. Space Weather Space Clim., 8, A31.
https://doi.org/10.1051/swsc/2018010
"""

__version__ = "1.0.0"
__author__ = "MAIRE-S Team"

from .core import (
    band_function_jiggins,
    energy_to_rigidity_proton,
    rigidity_to_energy_proton,
    convert_dJ_dR_to_dJ_dE,
)

from .spectra import (
    generate_sapphire_spectra,
    get_sapphire_parameters,
    SAPPHIRE_EVENTS,
)

from .plotting import (
    plot_spectra_rigidity,
    plot_spectra_energy,
    plot_both_spaces,
)

__all__ = [
    # Core functions
    "band_function_jiggins",
    "energy_to_rigidity_proton",
    "rigidity_to_energy_proton",
    "convert_dJ_dR_to_dJ_dE",
    
    # Spectra generation
    "generate_sapphire_spectra",
    "get_sapphire_parameters",
    "SAPPHIRE_EVENTS",
    
    # Plotting
    "plot_spectra_rigidity",
    "plot_spectra_energy",
    "plot_both_spaces",
]
