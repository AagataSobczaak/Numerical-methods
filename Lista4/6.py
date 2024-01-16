import numpy as np
import cmath
from scipy.optimize import fsolve

# Obliczanie wartości wielomianu, wartości pochodnej oraz drugiej pochodnej w punkcie x
def wartosci_wiel(a,x):

    n = len(a) - 1
    wartość_wielomianu = a[n]
    pierwsza_pochodna = 0.0 + 0.0j
    druga_pochodna = 0.0 + 0.0j
    
    for i in range(1,n+1):
        # używamy wzorów różnicowych w celu obliczenia drugiej pochodnej
        druga_pochodna = druga_pochodna * x + 2.0 * pierwsza_pochodna
        pierwsza_pochodna = pierwsza_pochodna * x + wartość_wielomianu
        wartość_wielomianu = wartość_wielomianu * x + a[n-i]
    return wartość_wielomianu,pierwsza_pochodna,druga_pochodna

# Główna funkcja obliczająca pierwiastki rzeczywiste i zespolone wielomianu
def pierwiastki_wiel(a):
    tol=1.0e-12
    # Metoda Laguerre'a do znalezienia pojedynczego pierwiastka wielomianu a
    def laguerre(a):
        
        # numeryczne przybliżanie wartości pierwiastka x 
        x = 0
        n = len(a) - 1
        for i in range(100):
            wartość_wielomianu, pierwsza_pochodna, druga_pochodna = wartosci_wiel(a,x)
            
            if abs(wartość_wielomianu) < tol:
                return x
            
            g = pierwsza_pochodna / wartość_wielomianu # wzór podany na wykładzie 
            h = g * g - druga_pochodna / wartość_wielomianu
            f = cmath.sqrt((n - 1) * (n * h - g * g))

            if abs(g + f) > abs(g - f): # znak dobieramy tak, aby poprawka |z_k-+1 - z_k| była jak  najmniejsza
                dx = n / (g + f)
            else:
                dx = n / (g - f)
            x = x - dx
            if abs(dx) < tol: # żeby nie było w nieszkończoność pętli
                return x
        print('Zbyt wiele iteracji')

    # Podział wielomianu poprzez wykorzystanie pojedynczego miejsca zerowego
    def deflPoly(a,pierwiastek):

        n = len(a)-1
        # Podzielony wielomian jest stopien mniejszy od wyjsciowego 
        b = [(0.0 + 0.0j)] * n
        b[n-1] = a[n]

        for i in range(n-2,-1,-1):
            b[i] = a[i+1] + pierwiastek * b[i+1]
        return b

    n = len(a) - 1
    # Lista na pierwiastki wielomianu a 
    pierwiastki = np.zeros(n,dtype = complex) # zera z rzeczywistymi i zespolonymi
    for i in range(n):
        x = laguerre(a)
        if abs(x.imag) < tol: x = x.real

        pierwiastki[i] = x
        a = deflPoly(a,x)

    return pierwiastki

c = np.array([-84.0,(30.0-14.0j),-(8.0-5.0j),(5.0+1.0j),1.0])

wynik = pierwiastki_wiel(c)

print(f"Miejscami zerowymi podanego wielomianu są: {list(wynik)}")
