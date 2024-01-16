sign_bit = "0"  # znak
exponent_bits = "01111111"  # wykładnik
fraction_bits = "10110011001100110011001"  # część ułamkowa

# Obliczamy wykładnik

exponent = 0  
fraction = 1  
for bit in fraction_bits:
    fraction += int(bit) * 2 ** (-1) 

real_value = (-1) ** int(sign_bit) * fraction * 2 ** exponent

# Obliczamy błędy
actual_value = 1.7
absolute_error = abs(actual_value - real_value)
relative_error = absolute_error / abs(actual_value)

print(f"Wartość liczby: {actual_value}")
print(f"IEEE-754: {real_value}")
print(f"Błąd bezwzględny: {absolute_error}")
print(f"Błąd względny: {relative_error}")