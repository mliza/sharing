import numpy as np

def shock(M1) 
    g = 1.4
    M2 = np.sqrt(((g- 1) * M1**2 +2)/ (2 * g * M1**2 - g + 1))
    P= (2 *g * M1**2- g +1) * ((g - 1) * M1**2 +2) / (g+1) 
    T =(2*g *M1**2 - g + 1) * ((g -1 ) *M1**2 +2) / ((g+1) * M1)**2 
    Rho = (g + 1)* M1**2 / (( g-1)*M1**2 +2)
    out = {'M2' :M2, 'P': P, 'T':T, 'Rho':Rho}
    return out
