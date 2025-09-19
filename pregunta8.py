"""
Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
"""
print("Serie de Fibonacci entre 0 y 50:")
a, b = 0, 1  # Semilla de Fibonacci

while a <= 50:
    print(a)          # Imprime el número actual (0, 1, 1, 2, 3, 5...)
    a, b = b, a + b   # Avanza al siguiente número de la serie