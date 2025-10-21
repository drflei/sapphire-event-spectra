"""
Quick test script to verify the sapphire-event-spectra package installation.
"""

import sys

def test_import():
    """Test that the package can be imported."""
    try:
        import sapphire_event_spectra as ses
        print("✅ Package imported successfully")
        print(f"   Version: {ses.__version__}")
        return True
    except ImportError as e:
        print(f"❌ Failed to import package: {e}")
        return False


def test_functions():
    """Test that core functions are available."""
    import sapphire_event_spectra as ses
    
    functions = [
        'band_function_jiggins',
        'energy_to_rigidity_proton',
        'rigidity_to_energy_proton',
        'convert_dJ_dR_to_dJ_dE',
        'generate_sapphire_spectra',
        'get_sapphire_parameters',
        'plot_spectra_rigidity',
        'plot_spectra_energy',
        'plot_both_spaces',
    ]
    
    all_ok = True
    for func_name in functions:
        if hasattr(ses, func_name):
            print(f"✅ Function '{func_name}' available")
        else:
            print(f"❌ Function '{func_name}' not found")
            all_ok = False
    
    return all_ok


def test_generate_spectra():
    """Test generating spectra."""
    import sapphire_event_spectra as ses
    
    try:
        # Generate a single event
        spectra = ses.generate_sapphire_spectra(
            events=['1-in-100-year'],
            E_min=1.0,
            E_max=1000.0,
            n_points=50
        )
        
        if '1-in-100-year' in spectra:
            data = spectra['1-in-100-year']
            required_keys = ['energy_MeV', 'rigidity_GV', 'fluence_dJ_dR', 
                           'fluence_dJ_dE', 'flux_dJ_dR', 'flux_dJ_dE']
            
            for key in required_keys:
                if key not in data:
                    print(f"❌ Missing key '{key}' in spectrum data")
                    return False
            
            print("✅ Spectrum generation successful")
            print(f"   Generated {len(data['energy_MeV'])} data points")
            return True
        else:
            print("❌ Expected event not found in results")
            return False
            
    except Exception as e:
        print(f"❌ Failed to generate spectra: {e}")
        return False


def test_parameters():
    """Test getting parameters."""
    import sapphire_event_spectra as ses
    
    try:
        df_params, gb_fluence, gb_flux = ses.get_sapphire_parameters()
        
        if len(df_params) == 7:
            print("✅ Parameters loaded successfully")
            print(f"   Number of events: {len(df_params)}")
            print(f"   gb_fluence: {gb_fluence}")
            print(f"   gb_flux: {gb_flux}")
            return True
        else:
            print(f"❌ Expected 7 events, got {len(df_params)}")
            return False
            
    except Exception as e:
        print(f"❌ Failed to get parameters: {e}")
        return False


def test_conversions():
    """Test energy-rigidity conversions."""
    import sapphire_event_spectra as ses
    import numpy as np
    
    try:
        # Test conversion
        E_test = np.array([10.0, 100.0, 1000.0])
        R = ses.energy_to_rigidity_proton(E_test)
        E_back = ses.rigidity_to_energy_proton(R)
        
        # Check round-trip accuracy
        if np.allclose(E_test, E_back, rtol=1e-10):
            print("✅ Energy-rigidity conversions working correctly")
            return True
        else:
            print("❌ Conversion round-trip failed")
            return False
            
    except Exception as e:
        print(f"❌ Failed conversion test: {e}")
        return False


def main():
    """Run all tests."""
    print("="*70)
    print("SAPPHIRE Event Spectra Package - Quick Test")
    print("="*70)
    print()
    
    tests = [
        ("Import", test_import),
        ("Functions", test_functions),
        ("Conversions", test_conversions),
        ("Parameters", test_parameters),
        ("Spectra Generation", test_generate_spectra),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        print("-"*70)
        results.append(test_func())
    
    print("\n" + "="*70)
    print("Test Summary:")
    print("="*70)
    
    for (test_name, _), result in zip(tests, results):
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
    
    all_passed = all(results)
    print("="*70)
    
    if all_passed:
        print("\n🎉 All tests passed!")
        return 0
    else:
        print("\n⚠️  Some tests failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
