import numpy as np 
import cProfile

def solve():
    
    # Parametry wejściowe
    n = 20
    A = np.zeros((n,n)) 
    I = np.zeros((n,n))
    b = np.zeros(n)
    x = np.zeros(n)

    # Wypełnienie macierzy A podanej w zadaniu i wektora b
    for i in range(n):
        A[i, i] = 4 # macierz
        I[i, i] = 1 
        if i > 0:
            A[i, i - 1] = -1
        if i < n - 1:
            A[i, i + 1] = -1
        if i == n - 1:
            A[1,i] = 1
            A[i,1] = 1  
            b[i] = 100 # wektor


    return np.linalg.solve(A ,b) # funkcja wbudowana rozwiązująca układ

# Nakład obliczeń i czas 
cProfile.run("solve()") 