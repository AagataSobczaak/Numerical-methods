import numpy as np
from scipy.special import roots_legendre

# Funkcja, którą całkujemy
def funkcja_do_całkowania(x):
    return np.log(x) / (x**2 - 2 * x + 2)

# Metoda Gaussa-Legendre'a
def gauss_legendre(func, a, b, węzły):
    
    xk, Ak = roots_legendre(węzły) # funkcja wbudowana do obliczania współczynników

    tk = (b - a) / 2 * xk + (b + a) / 2 

    wynik = (b - a) / 2 * sum(Ak * func(tk))
    return wynik

# Przedziały
a = 1
b = np.pi


# Obliczenia
węzły_2 = gauss_legendre(funkcja_do_całkowania,a,b,2)
węzły_4 = gauss_legendre(funkcja_do_całkowania,a,b,4)

# Wydrukuj wyniki
print(f"Wynik dla 2 węzłów: {węzły_2}")
print(f"Wynik dla 4 węzłów: {węzły_4}")

