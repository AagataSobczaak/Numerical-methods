import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Dane 
Re_data = np.array([0.2, 2, 20, 200, 2000, 20000])
cD_data = np.array([103, 13.9, 2.72, 0.8, 0.401, 0.433])
Re_values = np.array([5, 50, 5000]) # liczba Reynoldsa do interpolacji

# Funkcja sklejana wbudowana
spline_function = CubicSpline(Re_data, cD_data) 

# Obliczenie współczynnika cD dla podanych wartości Re
cD_values = spline_function(Re_values)

print(f"Dla {Re_values} wartości wynoszą {cD_values}")

x = np.linspace(0,21000,10)
y = spline_function(x)

plt.plot(x,y)
plt.scatter(Re_data,cD_data, c = 'g', label = "Dane")
plt.scatter(Re_values,cD_values, c = 'b', label = "Liczba Reynoldsa")
plt.legend()
plt.show()














#Interpolacja – ma przechodzić przez punkty, aproksymacja wartości funkcji w jakimś zakresie zmiennych na podstawie części wartości z tego zakresu