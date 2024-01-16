import numpy as np

masa_auta = 2000
v_wartosci = [0,1,1.8,2.4,3.5,4.4,5.1,6]
P_wartosci = [0, 4700, 12200, 19000, 31800, 40100, 43800, 43200]

# wzór z wykładu 
def lagrange(x,xData,yData): # najpierw sobie interpolujemy funkcje mocy
    n = len(xData)
    y = 0
    for i in range(n):
        w = 1.0
        for j in range(n):
            if i != j:
                w = w * (x - xData[j]) / (xData[i] - xData[j])
        y = y + w * yData[i]
    return y

def czas_rozpędu(v):
    return masa_auta * v / lagrange(v,v_wartosci,P_wartosci) # nasza funkcja podcałkowa z interpolowaną funkcję P

# Wzór Simpsona z wykładu

def simpson(f,a,b,N=50):
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b - a) / N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])
    return S

print(f"Czas rozpędzenia: {simpson(czas_rozpędu,v_wartosci[1],v_wartosci[-1])}")
