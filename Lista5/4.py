import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Dane
x_data = np.array([1.2, 2.8, 4.3, 5.4, 6.8, 7.9])
y_data = np.array([7.5, 16.1, 38.9, 67.0, 146.6, 266.2])

# Model funkcji aproksymującej
def model_function(x, a, b):
    return a * np.exp(b * x)


### FUNKCJA WBUDOWANA ###

# Dopasowanie funkcji przy użyciu curve_fit
params, covariance = curve_fit(model_function, x_data, y_data)

# Parametry a i b
a1, b1 = params

# Obliczenie wartości funkcji aproksymującej
y_fit1 = model_function(x_data, a1, b1)

# Obliczenie odchylenia standardowego
residuals = y_data - y_fit1
std_dev1 = np.std(residuals)

# Wyświetlenie wyników
print(f"Parametry a i b funkcji wbudowanej:a =, {a1},b = {b1}, odchylenie standardowe: {std_dev1}")

### WŁASNA IMPLEMENTACJA ###

#Transormujemy
ydata_ln = np.log(y_data)

#Liczymy średnie
xdata_mean = np.mean(x_data)
ydata_ln_mean = np.mean(ydata_ln)
ydata_mean = np.mean(y_data)

# Obliczamy współczynniki regresji liniowej metoda największych kwadratów
b_1 = np.sum((x_data - xdata_mean) * ydata_ln) / np.sum((x_data - xdata_mean) ** 2)
b_0 = ydata_ln_mean - b_1 * xdata_mean

# Obliczamy współczynniki a i b do funkcji eksponencjalnej
a = np.exp(b_0)
b = b_1

# Obliczenie odchylenia standardowego
y_fit = model_function(x_data, a, b)
std_dev = np.std(y_data - y_fit)

# Wyświetlenie wyników
print(f"Parametry a i b funkcji własnej implementacji:a =, {a},b = {b}, odchylenie standardowe: {std_dev}")

# Wykres
x= np.arange(min(x_data), max(x_data), 0.02)
plt.scatter(x_data, y_data, color = "b", label = "Dane")
plt.plot(x, a * np.exp(b * x), color = "g",label = "Aproksymacja:f(x)")
plt.legend()
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
