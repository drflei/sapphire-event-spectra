"""
Plotting utilities for SAPPHIRE event spectra.

This module provides convenient functions for visualizing SAPPHIRE spectra
in both rigidity and energy space.
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_spectra_rigidity(
    spectra_results,
    events=None,
    figsize=(16, 6),
    xlim=(0.01, 100),
    ylim_fluence=None,
    ylim_flux=None,
    show=True,
):
    """
    Plot SAPPHIRE spectra in rigidity space (dJ/dR vs R).
    
    Parameters
    ----------
    spectra_results : dict
        Dictionary from generate_sapphire_spectra()
    events : list of str, optional
        Subset of events to plot. If None, plots all events.
    figsize : tuple, default=(16, 6)
        Figure size (width, height) in inches
    xlim : tuple, default=(0.01, 100)
        X-axis limits (Rigidity in GV)
    ylim_fluence : tuple, optional
        Y-axis limits for fluence panel
    ylim_flux : tuple, optional
        Y-axis limits for flux panel
    show : bool, default=True
        Whether to call plt.show()
    
    Returns
    -------
    fig : matplotlib.figure.Figure
        The created figure
    axes : array of matplotlib.axes.Axes
        The axes objects [ax_fluence, ax_flux]
    """
    # Default color palette
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']
    
    # Determine which events to plot
    if events is None:
        events = list(spectra_results.keys())
    
    # Create color map
    color_map = {event: colors[i % len(colors)] for i, event in enumerate(events)}
    
    # Create figure
    fig, axes = plt.subplots(1, 2, figsize=figsize)
    ax1, ax2 = axes
    
    # Panel 1: Event-integrated fluence (dJ/dR)
    for event in events:
        if event not in spectra_results:
            print(f"Warning: Event '{event}' not found in spectra_results")
            continue
        
        data = spectra_results[event]
        if 'fluence_dJ_dR' in data:
            ax1.loglog(
                data['rigidity_GV'],
                data['fluence_dJ_dR'],
                color=color_map[event],
                linewidth=2.5,
                label=f'SAPPHIRE {event}',
                alpha=0.9
            )
    
    ax1.set_xlabel('Rigidity (GV)', fontsize=13, fontweight='bold')
    ax1.set_ylabel('dJ/dR (particles/cm²/sr/GV)', fontsize=12, fontweight='bold')
    ax1.set_title('Event-Integrated Fluence Spectra', fontsize=14, fontweight='bold')
    ax1.grid(True, which='both', alpha=0.3)
    ax1.legend(fontsize=10, loc='best')
    ax1.set_xlim(xlim)
    if ylim_fluence:
        ax1.set_ylim(ylim_fluence)
    
    # Panel 2: Event peak flux (dJ/dR)
    for event in events:
        if event not in spectra_results:
            continue
        
        data = spectra_results[event]
        if 'flux_dJ_dR' in data:
            ax2.loglog(
                data['rigidity_GV'],
                data['flux_dJ_dR'],
                color=color_map[event],
                linewidth=2.5,
                label=f'SAPPHIRE {event}',
                alpha=0.9
            )
    
    ax2.set_xlabel('Rigidity (GV)', fontsize=13, fontweight='bold')
    ax2.set_ylabel('dJ/dR (particles/cm²/sr/s/GV)', fontsize=12, fontweight='bold')
    ax2.set_title('Event Peak Flux Spectra', fontsize=14, fontweight='bold')
    ax2.grid(True, which='both', alpha=0.3)
    ax2.legend(fontsize=10, loc='best')
    ax2.set_xlim(xlim)
    if ylim_flux:
        ax2.set_ylim(ylim_flux)
    
    plt.tight_layout()
    
    if show:
        plt.show()
    
    return fig, axes


def plot_spectra_energy(
    spectra_results,
    events=None,
    figsize=(16, 6),
    xlim=(1, 1e5),
    ylim_fluence=None,
    ylim_flux=None,
    show=True,
):
    """
    Plot SAPPHIRE spectra in energy space (dJ/dE vs E).
    
    Parameters
    ----------
    spectra_results : dict
        Dictionary from generate_sapphire_spectra()
    events : list of str, optional
        Subset of events to plot. If None, plots all events.
    figsize : tuple, default=(16, 6)
        Figure size (width, height) in inches
    xlim : tuple, default=(1, 1e5)
        X-axis limits (Energy in MeV)
    ylim_fluence : tuple, optional
        Y-axis limits for fluence panel
    ylim_flux : tuple, optional
        Y-axis limits for flux panel
    show : bool, default=True
        Whether to call plt.show()
    
    Returns
    -------
    fig : matplotlib.figure.Figure
        The created figure
    axes : array of matplotlib.axes.Axes
        The axes objects [ax_fluence, ax_flux]
    """
    # Default color palette
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']
    
    # Determine which events to plot
    if events is None:
        events = list(spectra_results.keys())
    
    # Create color map
    color_map = {event: colors[i % len(colors)] for i, event in enumerate(events)}
    
    # Create figure
    fig, axes = plt.subplots(1, 2, figsize=figsize)
    ax1, ax2 = axes
    
    # Panel 1: Event-integrated fluence (dJ/dE)
    for event in events:
        if event not in spectra_results:
            print(f"Warning: Event '{event}' not found in spectra_results")
            continue
        
        data = spectra_results[event]
        if 'fluence_dJ_dE' in data:
            ax1.loglog(
                data['energy_MeV'],
                data['fluence_dJ_dE'],
                color=color_map[event],
                linewidth=2.5,
                label=f'SAPPHIRE {event}',
                alpha=0.9
            )
    
    ax1.set_xlabel('Energy (MeV)', fontsize=13, fontweight='bold')
    ax1.set_ylabel('dJ/dE (particles/cm²/sr/MeV)', fontsize=12, fontweight='bold')
    ax1.set_title('Event-Integrated Fluence Spectra', fontsize=14, fontweight='bold')
    ax1.grid(True, which='both', alpha=0.3)
    ax1.legend(fontsize=10, loc='best')
    ax1.set_xlim(xlim)
    if ylim_fluence:
        ax1.set_ylim(ylim_fluence)
    
    # Panel 2: Event peak flux (dJ/dE)
    for event in events:
        if event not in spectra_results:
            continue
        
        data = spectra_results[event]
        if 'flux_dJ_dE' in data:
            ax2.loglog(
                data['energy_MeV'],
                data['flux_dJ_dE'],
                color=color_map[event],
                linewidth=2.5,
                label=f'SAPPHIRE {event}',
                alpha=0.9
            )
    
    ax2.set_xlabel('Energy (MeV)', fontsize=13, fontweight='bold')
    ax2.set_ylabel('dJ/dE (particles/cm²/sr/s/MeV)', fontsize=12, fontweight='bold')
    ax2.set_title('Event Peak Flux Spectra', fontsize=14, fontweight='bold')
    ax2.grid(True, which='both', alpha=0.3)
    ax2.legend(fontsize=10, loc='best')
    ax2.set_xlim(xlim)
    if ylim_flux:
        ax2.set_ylim(ylim_flux)
    
    plt.tight_layout()
    
    if show:
        plt.show()
    
    return fig, axes


def plot_both_spaces(
    spectra_results,
    events=None,
    figsize=(16, 12),
    xlim_rigidity=(0.01, 100),
    xlim_energy=(1, 1e5),
    show=True,
):
    """
    Plot SAPPHIRE spectra in both rigidity and energy space.
    
    Creates a 2x2 grid:
    - Top row: Rigidity space (fluence, flux)
    - Bottom row: Energy space (fluence, flux)
    
    Parameters
    ----------
    spectra_results : dict
        Dictionary from generate_sapphire_spectra()
    events : list of str, optional
        Subset of events to plot. If None, plots all events.
    figsize : tuple, default=(16, 12)
        Figure size (width, height) in inches
    xlim_rigidity : tuple, default=(0.01, 100)
        X-axis limits for rigidity plots (GV)
    xlim_energy : tuple, default=(1, 1e5)
        X-axis limits for energy plots (MeV)
    show : bool, default=True
        Whether to call plt.show()
    
    Returns
    -------
    fig : matplotlib.figure.Figure
        The created figure
    axes : ndarray of matplotlib.axes.Axes
        2x2 array of axes objects
    """
    # Default color palette
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']
    
    # Determine which events to plot
    if events is None:
        events = list(spectra_results.keys())
    
    # Create color map
    color_map = {event: colors[i % len(colors)] for i, event in enumerate(events)}
    
    # Create figure
    fig, axes = plt.subplots(2, 2, figsize=figsize)
    
    # Top row: Rigidity space
    ax_rig_fluence, ax_rig_flux = axes[0, :]
    
    for event in events:
        if event not in spectra_results:
            continue
        data = spectra_results[event]
        
        if 'fluence_dJ_dR' in data:
            ax_rig_fluence.loglog(
                data['rigidity_GV'], data['fluence_dJ_dR'],
                color=color_map[event], linewidth=2.5,
                label=f'SAPPHIRE {event}', alpha=0.9
            )
        
        if 'flux_dJ_dR' in data:
            ax_rig_flux.loglog(
                data['rigidity_GV'], data['flux_dJ_dR'],
                color=color_map[event], linewidth=2.5,
                label=f'SAPPHIRE {event}', alpha=0.9
            )
    
    ax_rig_fluence.set_xlabel('Rigidity (GV)', fontsize=12, fontweight='bold')
    ax_rig_fluence.set_ylabel('dJ/dR (particles/cm²/sr/GV)', fontsize=11, fontweight='bold')
    ax_rig_fluence.set_title('Event Fluence - Rigidity Space', fontsize=13, fontweight='bold')
    ax_rig_fluence.grid(True, which='both', alpha=0.3)
    ax_rig_fluence.legend(fontsize=9, loc='best')
    ax_rig_fluence.set_xlim(xlim_rigidity)
    
    ax_rig_flux.set_xlabel('Rigidity (GV)', fontsize=12, fontweight='bold')
    ax_rig_flux.set_ylabel('dJ/dR (particles/cm²/sr/s/GV)', fontsize=11, fontweight='bold')
    ax_rig_flux.set_title('Peak Flux - Rigidity Space', fontsize=13, fontweight='bold')
    ax_rig_flux.grid(True, which='both', alpha=0.3)
    ax_rig_flux.legend(fontsize=9, loc='best')
    ax_rig_flux.set_xlim(xlim_rigidity)
    
    # Bottom row: Energy space
    ax_eng_fluence, ax_eng_flux = axes[1, :]
    
    for event in events:
        if event not in spectra_results:
            continue
        data = spectra_results[event]
        
        if 'fluence_dJ_dE' in data:
            ax_eng_fluence.loglog(
                data['energy_MeV'], data['fluence_dJ_dE'],
                color=color_map[event], linewidth=2.5,
                label=f'SAPPHIRE {event}', alpha=0.9
            )
        
        if 'flux_dJ_dE' in data:
            ax_eng_flux.loglog(
                data['energy_MeV'], data['flux_dJ_dE'],
                color=color_map[event], linewidth=2.5,
                label=f'SAPPHIRE {event}', alpha=0.9
            )
    
    ax_eng_fluence.set_xlabel('Energy (MeV)', fontsize=12, fontweight='bold')
    ax_eng_fluence.set_ylabel('dJ/dE (particles/cm²/sr/MeV)', fontsize=11, fontweight='bold')
    ax_eng_fluence.set_title('Event Fluence - Energy Space', fontsize=13, fontweight='bold')
    ax_eng_fluence.grid(True, which='both', alpha=0.3)
    ax_eng_fluence.legend(fontsize=9, loc='best')
    ax_eng_fluence.set_xlim(xlim_energy)
    
    ax_eng_flux.set_xlabel('Energy (MeV)', fontsize=12, fontweight='bold')
    ax_eng_flux.set_ylabel('dJ/dE (particles/cm²/sr/s/MeV)', fontsize=11, fontweight='bold')
    ax_eng_flux.set_title('Peak Flux - Energy Space', fontsize=13, fontweight='bold')
    ax_eng_flux.grid(True, which='both', alpha=0.3)
    ax_eng_flux.legend(fontsize=9, loc='best')
    ax_eng_flux.set_xlim(xlim_energy)
    
    plt.tight_layout()
    
    if show:
        plt.show()
    
    return fig, axes
