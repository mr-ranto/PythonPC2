"""
Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
"""
def fibonacci_hasta_50():
    #Genera la serie de Fibonacci entre 0 y 50
    a, b = 0, 1
    serie = []
    while a <= 50:
        serie.append(a)
        a, b = b, a + b
    return serie

# Llamar a la función
resultado = fibonacci_hasta_50()
print("Serie de Fibonacci (0-50):", resultado)