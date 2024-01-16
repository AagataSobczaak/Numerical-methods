import numpy as np

def lagrange(x, xData, yData):
    n = len(xData)
    y = 0
    for i in range(n):
        w = 1.0
        for j in range(n):
            if i != j:
                w = w * (x-xData[j]) / (xData[i] - xData[j])
        y = y + w * yData[i]
    return y


# Obliczenia dla wielomianu interpolacyjnego
xData = [-2.2, -0.3, 0.8, 1.9]
yData = [15.180, 10.962, 1.920, -2.040]

# Interpolacja wielomianowa dla punktów x
x_interpolated = 0

# Wartość wielomianu interpolacyjnego w punkcie x_interpolated
y_interpolated = lagrange(x_interpolated, xData, yData)
print(f"Wartość wielomianu interpolacyjnego w x={x_interpolated}: {y_interpolated}")

# Pochodna pierwszego rzędu f'(x_interpolated)
h = 0.001  # Mała zmiana x
pochodna_1 = (lagrange(x_interpolated + h, xData, yData) - lagrange(x_interpolated - h, xData, yData)) / (2 * h)
print(f"Pochodna pierwszego rzędu f'({x_interpolated}): {pochodna_1}")

# Pochodna drugiego rzędu f''(x_interpolated)
pochodna_2 = (lagrange(x_interpolated + h, xData, yData) - 2 * lagrange(x_interpolated, xData, yData) + lagrange(x_interpolated - h, xData, yData)) / (h**2)
print(f"Pochodna drugiego rzędu f''({x_interpolated}): {pochodna_2}")