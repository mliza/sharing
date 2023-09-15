'''
    Date:   09/08/2023
    Author: Martin E. Liza
    File:   normal_shock_relations
    Def:    Calculate the normal shock relations.

    Author		    Date		Revision
    ---------------------------------------------
    Martin E. Liza	09/08/2023	Initial version.
'''
import numpy as np

# REF: https://www.grc.nasa.gov/www/k-12/airplane/normal.html
# NOTE: var_r = var_1 / var_2 = var_preshock / var_postshock = [ ] 
def normal_shock_relations(mach_1, adiabatic_indx=1.4):
    # Defined to make calculations easy
    gamma_minus   = adiabatic_indx - 1
    gamma_plus    = adiabatic_indx + 1
    mach_11       = mach_1 ** 2
    
    mach_2        = np.sqrt( (gamma_minus * mach_11 + 2) /
                             (2 * adiabatic_indx * mach_11 - gamma_minus) )
    pressure_r    = (2 * adiabatic_indx * mach_11 - gamma_minus) / gamma_plus
    temperature_r = ( (2 * adiabatic_indx * mach_11 - gamma_minus) *
                      (gamma_minus * mach_11 + 2) / (gamma_plus**2 * mach_11) )
    density_r     = gamma_plus * mach_11 / (gamma_minus * mach_11 + 2)

    # Return Dictionary 
    normal_shock_dict = { 'mach_2'        : mach_2,
                          'pressure_r'    : pressure_r, 
                          'temperature_r' : temperature_r,
                          'density_r'     : density_r }
    return normal_shock_dict # [ ]
