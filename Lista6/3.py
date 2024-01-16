import numpy as np

# Funkcja do całkowania
def funkcja_z_podstawionym_t(t):
    return 1 / 3 * (1 / (1 + t**(4 / 3)))

# Granice całkowania po podstawieniu
a = 0
b = 1

# Węzły trapezów
n = 6

# Metoda trapezów
def metoda_trapezów(fun, a, b, n):
  
  Pole_trapezu = 0
 
  h  = (b - a) / n
 
  for i in range(n):
    fa = a + h * i
    fb = a + h * (i + 1)
 
    Pole_trapezu += (fun(fa) + fun(fb)) * h  / 2
  return Pole_trapezu
 
wynik = metoda_trapezów(funkcja_z_podstawionym_t, 0, 1, 6)
print("Rozwiązanie całki wyznaczone metodą trapezów:", wynik)



