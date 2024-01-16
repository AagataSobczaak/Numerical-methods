import numpy as np 
from numpy import sign
import math
from scipy.optimize import fsolve
# Stałe

R = 8.31441 # J/K 
T_0 = 4.44418 # K 
G = -10**5
a = 1
b = 1000


def gibbs(T):
    return G + R * T * np.log( ( T / T_0 ) ** ( 2.5 ) )

def szukana_temperatura():

    # Zakładamy pewny przedział, w którym szukamy rozwiązania
    dolny_punkt = a
    górny_punkt = b

    if gibbs(dolny_punkt) == 0.0:
        return dolny_punkt
    
    if gibbs(górny_punkt) == 0.0:
        return górny_punkt 
    
    # Ustalamy tolerancję błędu
    tol = 1.0e-9
    switch = 1 # z wykładu: sprawdzamy czy funkcja f_3(x) maleje z każdym krokiem
    
    n = int(math.ceil(math.log(abs(b - a) / tol)/math.log(2.0))) # z wykładu
    
    # Implementacja metody bisekcji
    for i in range(n):

        środek = (dolny_punkt + górny_punkt) / 2.0
        
        if (switch == 1) and abs(gibbs(środek)) > abs(gibbs(dolny_punkt) ) and abs(gibbs(środek) > abs(gibbs(górny_punkt))): # z wykładu
            return None
        
        if gibbs(środek) == 0.0:
            return środek
        
        if gibbs(górny_punkt) * gibbs(środek) < 0:
            dolny_punkt = środek
        
        else:
            górny_punkt = środek

    return (dolny_punkt + górny_punkt) / 2.0

# Znajdujemy temperaturę
wynik = szukana_temperatura()

print(f'Temperatura, dla której G = -10^5 J, wynosi {wynik:.4f} K')


# sprawdzenie funkcją wbudowaną
y = lambda T: G + R * T * np.log( ( T / T_0 ) ** ( 2.5 ) )
result_builtin = fsolve(y, [904, 905])
print(f"Wynik z funkcji wbudowanej: {result_builtin}")