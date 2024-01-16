import numpy as np
import scipy.linalg as sl


n = 5 # Rozmiar macierzy
A = np.array(sl.hilbert(n)) # Macierz Hilberta
b = np.array([5, 4, 3, 2, 1], dtype=np.float32).T # Wektor b


# Funkcja iteracyjnego rozwiązania
def iter_solve(A, b, n):
    LU, piv = sl.lu_factor(A) # rozkład LU macierzy A 
    x = np.zeros(n, dtype = np.float32) # tworzymy wektor rozwiązania x i dajemy float32 dla pojedynczej precyzji
    u = np.finfo(float).eps #Ustawiamy epsilon maszynowy jako tolerancję dla zbieżności, czyli to tolerancja dla warunku zakonczenia iteracji: najmniejsza liczba, taka że  1.0 + eps != 1.0. # to nasza dokładność
    iterations = 0 
    while True: 
        r = b - np.dot(A, x) # Wektor reszt r 
        if np.linalg.norm(r, np.inf) <= u * np.linalg.norm(b, np.inf) or iterations == 1000:  #Warunek zakończenia na podstawie normy reszty lub ilości iteracji, żeby uniknąć nieskończonej pętli
            break
        delta_x = sl.lu_solve((LU, piv), r)  # obliczanie poprawki używając rozkładu LU
        x = x + delta_x 
        iterations += 1
    return x

print(iter_solve(A,b,n))
