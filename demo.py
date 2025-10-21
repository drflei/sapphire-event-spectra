"""
Quick demo of sapphire-event-spectra package functionality.
This script can be run directly without installing the package.
"""

import sys
import os

# Add the package directory to Python path
package_dir = os.path.join(os.path.dirname(__file__), 'sapphire_event_spectra')
sys.path.insert(0, os.path.dirname(__file__))

# Now import the package
import sapphire_event_spectra as ses
import matplotlib.pyplot as plt

def main():
    print("="*80)
    print("SAPPHIRE Event Spectra - Quick Demo")
    print("="*80)
    print()
    
    # 1. Show available events
    print("Available SAPPHIRE events:")
    for event in ses.SAPPHIRE_EVENTS:
        print(f"  • {event}")
    print()
    
    # 2. Get parameters
    print("Loading SAPPHIRE parameters from Table 8...")
    df_params, gb_fluence, gb_flux = ses.get_sapphire_parameters()
    print(f"✅ Loaded parameters for {len(df_params)} events")
    print(f"   Common gamma_beta (fluence): {gb_fluence}")
    print(f"   Common gamma_beta (flux): {gb_flux}")
    print()
    
    # 3. Generate spectra
    print("Generating spectra for selected events...")
    selected_events = ['1-in-100-year', '1-in-1000-year', '1-in-10000-year']
    
    spectra = ses.generate_sapphire_spectra(
        events=selected_events,
        E_min=1.0,
        E_max=1e4,
        n_points=150
    )
    print(f"✅ Generated spectra for {len(spectra)} events")
    print()
    
    # 4. Show data for one event
    event_data = spectra['1-in-100-year']
    print("Data available for '1-in-100-year' event:")
    for key in event_data.keys():
        if key != 'parameters':
            if hasattr(event_data[key], '__len__'):
                print(f"  • {key}: array with {len(event_data[key])} points")
            else:
                print(f"  • {key}")
    print()
    
    print("Parameters for '1-in-100-year' event:")
    params = event_data['parameters']
    print(f"  Fluence: ga={params['fluence']['ga']}, gb={params['fluence']['gb']}, "
          f"R0={params['fluence']['R0']:.4f} GV, Rb={params['fluence']['Rb']:.4f} GV")
    print(f"  Flux:    ga={params['flux']['ga']}, gb={params['flux']['gb']}, "
          f"R0={params['flux']['R0']:.4f} GV, Rb={params['flux']['Rb']:.4f} GV")
    print()
    
    # 5. Test energy-rigidity conversion
    print("Testing energy-rigidity conversion:")
    import numpy as np
    E_test = np.array([10.0, 100.0, 1000.0])
    R_test = ses.energy_to_rigidity_proton(E_test)
    for E, R in zip(E_test, R_test):
        print(f"  {E:8.1f} MeV  →  {R:8.4f} GV")
    print()
    
    # 6. Create plots
    print("Creating plots...")
    
    # Energy space plot
    print("  1. Plotting in energy space...")
    fig1, axes1 = ses.plot_spectra_energy(spectra, show=False)
    plt.savefig('sapphire_energy_space.png', dpi=150, bbox_inches='tight')
    print("     ✅ Saved: sapphire_energy_space.png")
    plt.close()
    
    # Rigidity space plot
    print("  2. Plotting in rigidity space...")
    fig2, axes2 = ses.plot_spectra_rigidity(spectra, show=False)
    plt.savefig('sapphire_rigidity_space.png', dpi=150, bbox_inches='tight')
    print("     ✅ Saved: sapphire_rigidity_space.png")
    plt.close()
    
    # Both spaces plot
    print("  3. Plotting both spaces...")
    fig3, axes3 = ses.plot_both_spaces(spectra, show=False)
    plt.savefig('sapphire_both_spaces.png', dpi=150, bbox_inches='tight')
    print("     ✅ Saved: sapphire_both_spaces.png")
    plt.close()
    
    print()
    print("="*80)
    print("Demo completed successfully! 🎉")
    print("="*80)
    print()
    print("Generated files:")
    print("  • sapphire_energy_space.png")
    print("  • sapphire_rigidity_space.png")
    print("  • sapphire_both_spaces.png")
    print()
    print("To use the package in your own code:")
    print("  1. Install: pip install -e .")
    print("  2. Import: import sapphire_event_spectra as ses")
    print("  3. Use: spectra = ses.generate_sapphire_spectra()")
    print()
    print("See examples.ipynb for more detailed usage examples.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
