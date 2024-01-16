solution = 7 / 100 * 100 - 7 

print(f"{solution}")

# Wynik tego działania jest liczbą bliską zeru, aczkolwiek przez reprezentacje liczb zmiennoprzecinkowych w komputerach i niedokładności arytmetyki zmiennoprzecinkowej nie jest to 
# oczekiwany przez nas wynik 0. 

#W komputerach liczby zmiennoprzecinkowe są przechowywane w formie liczb binarnych z użyciem skończonej liczby bitów. Niektóre liczby dziesiętne nie mogą być dokładnie 
# reprezentowane w tej formie, co prowadzi do błędów zaokrągleń. W szczególności liczby dziesiętne, które mają nieskończoną reprezentację dziesiętną (na przykład 1/3), 
# nie mogą być dokładnie przedstawione w formie binarnej.


numbers = []

for i in range(1, 51):
    result = i / 100 * 100 - i
    if result != 0:
        numbers.append(i)

print("Liczby podatne na błąd:", numbers)
