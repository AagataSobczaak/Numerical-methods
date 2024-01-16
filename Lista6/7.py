import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Metoda Lagrange do interpolacji
def lagrange(x, xData, yData):
    n = len(xData)
    y = 0
    for i in range(n):
        w = 1.0
        for j in range(n):
            if i != j:
                w = w * (x - xData[j]) / (xData[i] - xData[j])
        y = y + w * yData[i]
    return y


xData = [0.0, 0.1, 0.2, 0.3, 0.4]
yData = [0.000000, 0.078348, 0.138910, 0.192916, 0.244981]

nasz_x = 0.2

# Pochodna pierwszego rzędu f'(0.2)
h = 0.001  # Mała zmiana x im mniejsze  h tym bardziej sie zblizamy
pochodna_1 = (lagrange(nasz_x + h, xData, yData) - lagrange(nasz_x - h, xData, yData)) / (2 * h) # iloraz różnicowy do policzenia wartosci w naszej pochodnej
print(f"Pochodna pierwszego rzędu f'({nasz_x}): {pochodna_1}")


