import numpy as np

def shock(M1) 
    gamma = 1.4
    M2 = np.sqrt(((gamma- 1) * M1**2 +2)/ (2 * gamma * M1**2 - gamma + 1))
    P= (2 *gamma * M1**2- gamma +1) * ((gamma - 1) * M1**2 +2) / (gamma+1) 
    T =(2*gamma *M1**2 - gamma + 1) * ((gamma -1 ) *M1**2 +2) / ((gamma+1) * M1)**2 
    Rho = (gamma + 1)* M1**2 / (( gamma-1)*M1**2 +2)
    out = {'M2' :M2, 'P': P, 'T':T, 'Rho':Rho}
    return out
