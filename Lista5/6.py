import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import linregress
import matplotlib.pyplot as plt

# Dane
x_data = np.array([1.0, 2.5, 3.5, 4.0, 1.1, 1.8, 2.2, 3.7])
y_data = np.array([6.008, 15.722, 27.13, 33.772, 5.257, 9.549, 11.098, 28.828])


### FUNKCJE WBUDOWANE ### 

def linear_function(x, a, b):
    return a * x + b

def quadratic_function(x, a, b, c):
    return a * x**2 + b * x + c

# Dopasowanie funkcji liniowej
params_linear, covariance_linear = curve_fit(linear_function, x_data, y_data)
a_linear, b_linear = params_linear

# Współczynnik determinacji R^2
slope, intercept, r_value, p_value, std_err = linregress(x_data, y_data)
r_squared = r_value**2

# Dopasowanie funkcji kwadratowej
params_quadratic, covariance_quadratic = curve_fit(quadratic_function, x_data, y_data)
a_quadratic, b_quadratic, c_quadratic = params_quadratic

# Współczynnik determinacji R^2
y_pred_quadratic = quadratic_function(x_data, a_quadratic, b_quadratic, c_quadratic)

ss_total = np.sum((y_data - np.mean(y_data))**2)
ss_residual = np.sum((y_data - y_pred_quadratic)**2)
r_squared_quadratic = 1 - (ss_residual / ss_total)


# Wyświetlanie wyników
print(f"Parametry funkcji liniowej metodą wbudowaną: a = {a_linear},b = {b_linear}, R^2 = {r_squared}")
print(f"Parametry funkcji kwadratowej metodą wbudowaną: a = {a_quadratic}, b = {b_quadratic}, c = {c_quadratic},R^2 = {r_squared_quadratic}")

# Wykres
x_range = np.linspace(min(x_data), max(x_data), 100)
y_linear = linear_function(x_range, a_linear, b_linear)
y_quadratic = quadratic_function(x_range, a_quadratic, b_quadratic, c_quadratic)

plt.scatter(x_data, y_data, label='Dane')
plt.plot(x_range, y_linear, label='Funkcja liniowa', c = "r")
plt.plot(x_range, y_quadratic, label='Funkcja kwadratowa', c = "g")
plt.legend()
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Metoda wbudowana: funkcja liniowa i kwadratowa')
plt.show()

### WŁASNA IMPLEMENTACJA ### 

# Funkcja liniowa
x_mean = np.mean(x_data) # metoda najmniejszych kwadratów
y_mean = np.mean(y_data)

a = np.sum((y_data - y_mean) * (x_data - x_mean)) / np.sum((x_data - x_mean) ** 2)
b = y_mean - a * x_mean

# Współczynnik determinacji R^2 dla prostej 
r_square = np.sum((a * x_data + b - y_mean) ** 2) / np.sum((y_data - y_mean) ** 2)

print(f"Parametry funkcji liniowej metodą własną: a = {a},b = {b}, R^2: {r_square}")


# Funkcja kwadratowa

A = np.array([[len(x_data), sum(x_data), sum(x_data**2)],
              [sum(x_data), sum(x_data**2), sum(x_data**3)],
              [sum(x_data**2), sum(x_data**3), sum(x_data**4)]])

B = np.array([sum(y_data), sum(x_data * y_data), sum(x_data**2 * y_data)])

ck, bk, ak = np.linalg.solve(A,B)

# Obliczamy R^2
y_mean = np.mean(y_data)
y_pred = ak * x_data**2 + bk * x_data + ck
ss_total = np.sum((y_data - y_mean)**2)
ss_residual = np.sum((y_data - y_pred)**2)
r_square1 = 1 - (ss_residual / ss_total)

print(f"Parametry funkcji kwadratowej metodą własną: a = {ak},b = {bk},c= {ck} R^2: {r_square1}")

# Wykres 
x= np.arange(min(x_data), max(x_data), 0.02)
plt.scatter(x_data, y_data, color = 'b', label = "Dane")
plt.plot(x, (x * a + b), c = "g", label = "Funkcja liniowa")
plt.plot(x,(ak * x**2 + bk * x + ck), c = "r", label = "Funkcja kwadratowa")
plt.grid()
plt.legend()
plt.title('Własna implementacja: Funkcja liniowa i kwadratowa')
plt.xlabel("x")
plt.ylabel("y")
plt.show()