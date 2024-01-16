import numpy as np
import cProfile

def Gauss_Seidel(A,b,x,n):   # używam wzoru podanego na tablicy
    L = np.tril(A)
    U = np.triu(A)
    D = np.diag(np.diag(A))
    Q = D + L
    inv_Q = np.linalg.inv(Q) 

    # promień spektralny
    M_GS = np.dot(U, -np.linalg.inv(D + L))
    M_GS_r = max(abs(np.linalg.eigvals(M_GS)))

    if M_GS_r < 1:
        print("Spełnia warunek zbieżności")
        print(M_GS_r)
    if M_GS_r >= 1:
        print("Nie spełnia warunku zbieżności")
    
    for i in range(n): # iteracyjne wyliczam x
        x = np.dot(inv_Q, np.dot((Q - A),x) + b)
    return x


# Parametry wejściowe
n = 20
A = np.zeros((n, n)) 
b = np.zeros(n)
x = np.zeros(n)

# Wypełnienie macierzy A podanej w zadaniu i wektora b
for i in range(n):
    A[i, i] = 4 # macierz

    if i > 0:
        A[i, i - 1] = -1 
    if i < n - 1:
        A[i, i + 1] = -1
    if i == n - 1: 
        A[1,i] = 1
        A[i,1] = 1 
        b[i] = 100 # wektor


# Rozwiązanie układu równań
print(f"Rozwiązanie: {Gauss_Seidel(A, b, x, n)}")

# Poprawny wynik
#right_solution = np.linalg.solve(A,b) # rozwiązanie układu funkcją wbudowaną
#print(f"Rozwiązanie funkcją wbudowaną: {right_solution}")

# Nakład obliczeń i czas 
cProfile.run("Gauss_Seidel(A,b,x,n)") 