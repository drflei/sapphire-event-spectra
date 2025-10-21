"""
SAPPHIRE spectra generation and parameter management.

This module provides functions to generate SAPPHIRE event spectra using
parameters from Table 8 of Jiggens et al. (2018).
"""

import numpy as np
import pandas as pd
from .core import (
    band_function_jiggins,
    energy_to_rigidity_proton,
    convert_dJ_dR_to_dJ_dE,
)


# Common gamma_beta (gb) values for ALL events (from "all" row in Table 8)
GB_EIFLU = 5.7   # for event-integrated fluence
GB_EPFLU = 5.25  # for event peak flux

# List of available SAPPHIRE events
SAPPHIRE_EVENTS = [
    "1-in-10-year",
    "1-in-20-year",
    "1-in-50-year",
    "1-in-100-year",
    "1-in-300-year",
    "1-in-1000-year",
    "1-in-10000-year",
]


def get_sapphire_parameters():
    """
    Get SAPPHIRE Band function parameters from Table 8 (Jiggens et al. 2018).
    
    Returns
    -------
    df_params : pd.DataFrame
        DataFrame containing Band function parameters for each event:
        - Event: Event return period identifier
        - ga_eiflu: gamma_alpha for event-integrated fluence
        - ga_epflu: gamma_alpha for event peak flux
        - R0_eiflu: Characteristic rigidity (GV) for fluence
        - R0_epflu: Characteristic rigidity (GV) for flux
        - C_eiflu: Normalization constant (particles/cm²/sr) for fluence
        - C_epflu: Normalization constant (particles/cm²/sr/s) for flux
    
    gb_eiflu : float
        Common gamma_beta for fluence (5.7)
    
    gb_epflu : float
        Common gamma_beta for flux (5.25)
    
    Notes
    -----
    The gamma_beta values are the same for all events and are returned
    separately from the DataFrame.
    
    References
    ----------
    Jiggens, P., et al. (2018). Table 8.
    J. Space Weather Space Clim., 8, A31.
    """
    sapphire_table8_params = {
        "Event": SAPPHIRE_EVENTS,
        
        # gamma_alpha (ga) - eiflu column
        "ga_eiflu": [0.85, 0.71, 0.56, 0.48, 0.38, 0.315, 0.195],
        
        # gamma_alpha (ga) - epflu column
        "ga_epflu": [2.55, 2.35, 2.18, 2.09, 1.99, 1.9, 1.77],
        
        # R0 (GV) - eiflu column
        "R0_eiflu": [7.22e-2, 7.01e-2, 6.81e-2, 6.71e-2, 6.58e-2, 6.50e-2, 6.36e-2],
        
        # R0 (GV) - epflu column
        "R0_epflu": [1.30e-1, 1.21e-1, 1.14e-1, 1.11e-1, 1.07e-1, 1.05e-1, 1.01e-1],
        
        # C (particles/cm²/sr) - eiflu column
        "C_eiflu": [1.33e10, 2.81e10, 5.85e10, 8.73e10, 1.45e11, 2.14e11, 3.95e11],
        
        # C (particles/cm²/sr/s) - epflu column
        "C_epflu": [6.03e3, 1.55e4, 3.58e4, 5.64e4, 9.60e4, 1.53e5, 2.96e5]
    }
    
    df_params = pd.DataFrame(sapphire_table8_params)
    
    return df_params, GB_EIFLU, GB_EPFLU


def generate_sapphire_spectra(
    events=None,
    E_min=0.1,
    E_max=1e5,
    n_points=200,
    include_fluence=True,
    include_flux=True,
):
    """
    Generate SAPPHIRE event spectra for specified events.
    
    Parameters
    ----------
    events : list of str, optional
        List of event identifiers to generate. If None, generates all events.
        Available events: '1-in-10-year', '1-in-20-year', '1-in-50-year',
        '1-in-100-year', '1-in-300-year', '1-in-1000-year', '1-in-10000-year'
    E_min : float, default=0.1
        Minimum energy in MeV
    E_max : float, default=1e5
        Maximum energy in MeV
    n_points : int, default=200
        Number of energy points (log-spaced)
    include_fluence : bool, default=True
        Include event-integrated fluence spectra
    include_flux : bool, default=True
        Include event peak flux spectra
    
    Returns
    -------
    spectra_results : dict
        Dictionary with event names as keys, each containing:
        - energy_MeV: Energy grid (MeV)
        - rigidity_GV: Rigidity grid (GV)
        - fluence_dJ_dR: Event fluence dJ/dR (particles/cm²/sr/GV)
        - fluence_dJ_dE: Event fluence dJ/dE (particles/cm²/sr/MeV)
        - flux_dJ_dR: Peak flux dJ/dR (particles/cm²/sr/s/GV)
        - flux_dJ_dE: Peak flux dJ/dE (particles/cm²/sr/s/MeV)
        - parameters: Dict with ga, gb, R0, C for fluence and flux
    
    Examples
    --------
    >>> # Generate all events
    >>> spectra = generate_sapphire_spectra()
    
    >>> # Generate specific events
    >>> spectra = generate_sapphire_spectra(
    ...     events=['1-in-100-year', '1-in-1000-year'],
    ...     E_min=1.0,
    ...     E_max=1e4
    ... )
    
    >>> # Access data
    >>> event_data = spectra['1-in-100-year']
    >>> energy = event_data['energy_MeV']
    >>> fluence = event_data['fluence_dJ_dE']
    """
    # Get parameters
    df_params, gb_eiflu, gb_epflu = get_sapphire_parameters()
    
    # Filter events if specified
    if events is not None:
        df_params = df_params[df_params['Event'].isin(events)].reset_index(drop=True)
        if len(df_params) == 0:
            raise ValueError(f"No valid events found. Available: {SAPPHIRE_EVENTS}")
    
    # Generate energy grid
    E_MeV = np.logspace(np.log10(E_min), np.log10(E_max), n_points)
    R_GV = energy_to_rigidity_proton(E_MeV)
    
    # Storage for results
    spectra_results = {}
    
    # Generate spectra for each event
    for idx, row in df_params.iterrows():
        event = row['Event']
        result = {
            'energy_MeV': E_MeV,
            'rigidity_GV': R_GV,
            'parameters': {}
        }
        
        # Event-integrated fluence spectrum
        if include_fluence:
            ga_eiflu = row['ga_eiflu']
            R0_eiflu = row['R0_eiflu']
            C_eiflu = row['C_eiflu']
            
            fluence_dJ_dR = band_function_jiggins(R_GV, ga_eiflu, gb_eiflu, R0_eiflu, C_eiflu)
            fluence_dJ_dE = convert_dJ_dR_to_dJ_dE(fluence_dJ_dR, E_MeV)
            
            result['fluence_dJ_dR'] = fluence_dJ_dR
            result['fluence_dJ_dE'] = fluence_dJ_dE
            result['parameters']['fluence'] = {
                'ga': ga_eiflu,
                'gb': gb_eiflu,
                'R0': R0_eiflu,
                'C': C_eiflu,
                'Rb': (gb_eiflu - ga_eiflu) * R0_eiflu  # Break rigidity
            }
        
        # Event peak flux spectrum
        if include_flux:
            ga_epflu = row['ga_epflu']
            R0_epflu = row['R0_epflu']
            C_epflu = row['C_epflu']
            
            flux_dJ_dR = band_function_jiggins(R_GV, ga_epflu, gb_epflu, R0_epflu, C_epflu)
            flux_dJ_dE = convert_dJ_dR_to_dJ_dE(flux_dJ_dR, E_MeV)
            
            result['flux_dJ_dR'] = flux_dJ_dR
            result['flux_dJ_dE'] = flux_dJ_dE
            result['parameters']['flux'] = {
                'ga': ga_epflu,
                'gb': gb_epflu,
                'R0': R0_epflu,
                'C': C_epflu,
                'Rb': (gb_epflu - ga_epflu) * R0_epflu  # Break rigidity
            }
        
        spectra_results[event] = result
    
    return spectra_results
