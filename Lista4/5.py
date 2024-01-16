import numpy as np
from scipy.optimize import fsolve

# Wielomian
def wielomian(x, y):
    return np.tan(x) - y - 1, np.cos(x) - 3 * np.sin(y)

# pochodne cząstkowe wielomianu podzielonego na f1 i f2
def f1(x, y):
    return np.tan(x) - y - 1

def pochodna_czastkowa_f1_po_x(x, y):
    return 1 / (np.cos(x))**2

def pochodna_czastkowa_f1_po_y(x, y):
    return -1

def f2(x, y):
    return np.cos(x) - 3 * np.sin(y)

def pochodna_czastkowa_f2_po_x(x, y):
    return -np.sin(x)

def pochodna_czastkowa_f2_po_y(x, y):
    return -3 * np.cos(y)

# wektor do metody Newtona
def wektor_f1_f2(x, y):
    return np.array([f1(x, y), f2(x, y)])

# Jakobian do metody Newtona
def jakobian(x, y):
    return np.array([[pochodna_czastkowa_f1_po_x(x, y), pochodna_czastkowa_f1_po_y(x, y)],
                     [pochodna_czastkowa_f2_po_x(x, y), pochodna_czastkowa_f2_po_y(x, y)]])

# Metoda Newtona do rozwiązań
def Newton(x, y):
    tol = 1.0e-9
    a = 0 # przedział taki sam dla x i y 
    b = 1.5

    n = int(np.ceil(np.log(abs(b - a) / tol) / np.log(2.0))) # z wykładu

    wyniki = np.array([])

    for i in range(n):

        J = jakobian(x, y)
        inv_jacobian = np.linalg.inv(J)

        [x,y] = [x,y] - np.dot(inv_jacobian, wektor_f1_f2(x, y))

    wyniki = np.append(wyniki, np.array([[x,y]]))
    return wyniki

print(f"Rozwiązanie [x,y] metodą Newtona wynosi:{Newton(0,0)}")


# Rozwiązanie funkcją wbudowaną
def rozwiązanie(zmienne):
    x, y = zmienne
    roz1 = np.tan(x) - y - 1
    roz2 = np.cos(x) - 3 * np.sin(y)
    return [roz1, roz2]

# Szukamy rozwiązań w przedziale (0, 1.5)
solution = fsolve(rozwiązanie, [0.0, 0.0])

print(f"Rozwiązanie układu równań: {solution}")

