import numpy as np

# D_c2(x,h) = (f(x+h) - f(x-h)) / 2h = f'(x) + O(h^2)

# D_c4(x,h) = 2^2 * D_c2(x,h) - D_c2(x,2h) = 3f'(x) + O(h^4)

# D_f1(x,h) = (f(x+h) - f(x)) / h


# # Definicja funkcji
# def f1(x):
#     return x**3 - 2*x

# def f2(x):
#     return np.sin(x)

# def f3(x):
#     return np.exp(x)

# Obliczanie przybliżonych pochodnych dla różnych wartości kroku
def oblicz_pochodne(funkcja, x, h):
    D_c2 = (funkcja(x + h) - funkcja(x - h)) / (2 * h)
    D_c4 = 4 * D_c2 - (funkcja(x + 2 * h) - funkcja(x - 2 * h)) / (4 * h)
    D_f1 = (funkcja(x + h) - funkcja(x)) / h
    return D_c2, D_c4, D_f1

# # Wartości x dla których obliczamy pochodne
# x1 = 1
# x2 = np.pi / 3
# x3 = 0

# # Różne wartości kroku
# h_values = [1, 0.1, 0.01, 0.001]

# # Obliczenia dla każdej funkcji i wartości x
# for funkcja in [f1, f2, f3]:
#     print(f"\nPochodne dla funkcji {funkcja.__name__}:")
#     for h in h_values:
#         D_c2, D_c4, D_f1 = oblicz_pochodne(funkcja, x1, h)
#         print(f"Dla h={h}:")
#         print(f"# D_c2(x,h) = {D_c2}, D_c4(x,h) = {D_c4}, D_f1(x,h) = {D_f1}")
#     print("-------")



import numpy as np

# Definicja funkcji
def f1(x):
    return x**3 - 2*x

def f2(x):
    return np.sin(x)

def f3(x):
    return np.exp(x)

# Pochodne analityczne
def pochodna_analityczna_f1(x):
    return 3 * x**2 - 2

def pochodna_analityczna_f2(x):
    return np.cos(x)

def pochodna_analityczna_f3(x):
    return np.exp(x)

# Obliczanie różnic między pochodną analityczną a wyliczonymi wartościami pochodnych
def oblicz_roznice(funkcja, pochodna_analityczna, x, h):
    D_c2, D_c4, D_f1 = oblicz_pochodne(funkcja, x, h)
    diff_D_c2 = np.abs(D_c2 - pochodna_analityczna(x))
    diff_D_c4 = np.abs(D_c4 - pochodna_analityczna(x))
    diff_D_f1 = np.abs(D_f1 - pochodna_analityczna(x))
    return diff_D_c2, diff_D_c4, diff_D_f1

# Wartości x dla których obliczamy pochodne
x1 = 1
x2 = np.pi / 3
x3 = 0

# Różne wartości kroku
h_values = [0.1, 0.01, 0.001]

# Obliczenia dla każdej funkcji i wartości x
for funkcja, pochodna_analityczna in zip([f1, f2, f3], [pochodna_analityczna_f1, pochodna_analityczna_f2, pochodna_analityczna_f3]):
    print(f"\nRóżnice dla funkcji {funkcja.__name__}:")
    for h in h_values:
        diff_D_c2, diff_D_c4, diff_D_f1 = oblicz_roznice(funkcja, pochodna_analityczna, x1, h)
        print(f"Dla h={h}:")
        print(f"Różnica D_f1: {diff_D_f1}, Różnica D_c2: {diff_D_c2}, Różnica D_c4: {diff_D_c4}")
    print("-------")