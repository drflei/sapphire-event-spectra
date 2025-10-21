"""
Core functions for SAPPHIRE event spectra calculations.

This module contains the fundamental Band function implementation and
energy-rigidity conversion utilities.
"""

import numpy as np


def band_function_jiggins(R, ga, gb, R0, C):
    """
    Band function for SAPPHIRE spectra (Jiggins et al. 2018).
    
    The Band function describes the differential rigidity spectrum:
    - For R ≤ Rb: dJ/dR = C·R^(-γa)·exp(-R/R0)
    - For R ≥ Rb: dJ/dR = C·R^(-γb)·[(γb - γa)·R0]^(γb-γa)·exp(γa - γb)
    
    where Rb = (γb - γa)·R0 is the break rigidity.
    
    Parameters
    ----------
    R : array-like
        Rigidity in GV (GigaVolts)
    ga : float
        gamma_alpha - low-rigidity spectral index
    gb : float
        gamma_beta - high-rigidity spectral index
    R0 : float
        Characteristic rigidity in GV
    C : float
        Normalization constant
        - For fluence: particles/cm²/sr
        - For flux: particles/cm²/sr/s
    
    Returns
    -------
    dJ_dR : ndarray
        Differential spectrum dJ/dR (per GV per steradian)
        - For fluence: particles/cm²/sr/GV
        - For flux: particles/cm²/sr/s/GV
    
    References
    ----------
    Jiggens, P., et al. (2018). J. Space Weather Space Clim., 8, A31.
    https://doi.org/10.1051/swsc/2018010
    """
    R = np.asarray(R, dtype=float)
    Rb = (gb - ga) * R0  # Break rigidity
    
    dJ_dR = np.zeros_like(R, dtype=float)
    
    # Low rigidity regime: R ≤ Rb
    low_mask = R <= Rb
    dJ_dR[low_mask] = C * R[low_mask]**(-ga) * np.exp(-R[low_mask] / R0)
    
    # High rigidity regime: R > Rb
    high_mask = R > Rb
    norm_factor = ((gb - ga) * R0)**(gb - ga) * np.exp(ga - gb)
    dJ_dR[high_mask] = C * R[high_mask]**(-gb) * norm_factor
    
    return dJ_dR


def energy_to_rigidity_proton(E_MeV):
    """
    Convert kinetic energy to rigidity for protons.
    
    Uses the relativistic relation:
    R [GV] = sqrt(E^2 + 2*E*m_p*c^2) / (Z*c)
    
    where m_p*c^2 = 938.272 MeV (proton rest mass energy)
    and Z = 1 (proton charge)
    
    Parameters
    ----------
    E_MeV : array-like
        Kinetic energy in MeV
    
    Returns
    -------
    R_GV : ndarray
        Rigidity in GV (GigaVolts)
    """
    m_p = 938.272  # Proton rest mass in MeV
    E = np.asarray(E_MeV, dtype=float)
    return np.sqrt(E**2 + 2 * E * m_p) / 1000.0  # Convert to GV


def rigidity_to_energy_proton(R_GV):
    """
    Convert rigidity to kinetic energy for protons.
    
    Inverse of energy_to_rigidity_proton.
    E = sqrt((R*Z)^2 + m_p^2) - m_p
    
    Parameters
    ----------
    R_GV : array-like
        Rigidity in GV (GigaVolts)
    
    Returns
    -------
    E_MeV : ndarray
        Kinetic energy in MeV
    """
    m_p = 938.272  # Proton rest mass in MeV
    R = np.asarray(R_GV, dtype=float)
    R_MeV = R * 1000.0  # Convert GV to MeV
    return np.sqrt(R_MeV**2 + m_p**2) - m_p


def convert_dJ_dR_to_dJ_dE(dJ_dR, E_MeV):
    """
    Convert differential spectrum from dJ/dR to dJ/dE.
    
    Uses the chain rule: dJ/dE = dJ/dR * dR/dE
    
    For protons:
    R = sqrt(E^2 + 2*E*m_p) / 1000 (in GV)
    dR/dE = (E + m_p) / (1000 * sqrt(E^2 + 2*E*m_p))  (in GV/MeV)
    
    Parameters
    ----------
    dJ_dR : array-like
        Differential spectrum dJ/dR
        - For fluence: particles/cm²/sr/GV
        - For flux: particles/cm²/sr/s/GV
    E_MeV : array-like
        Kinetic energy in MeV (must match shape of dJ_dR)
    
    Returns
    -------
    dJ_dE : ndarray
        Differential spectrum dJ/dE
        - For fluence: particles/cm²/sr/MeV
        - For flux: particles/cm²/sr/s/MeV
    """
    m_p = 938.272  # Proton rest mass in MeV
    E = np.asarray(E_MeV, dtype=float)
    dJ_dR = np.asarray(dJ_dR, dtype=float)
    
    # Calculate dR/dE
    dR_dE = (E + m_p) / (1000.0 * np.sqrt(E**2 + 2 * E * m_p))  # GV/MeV
    
    return dJ_dR * dR_dE
