"""
Problema 3:
Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
en el rango de 1500 y 2700 (ambos incluidos).
"""

for n in range(1500,2701):
    if n % 5 == 0 and n % 7 == 0:
        print(n)
        