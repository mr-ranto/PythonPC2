"""
Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
función acepta el número como argumento.
"""
# Número como argumento en la función

n = 5 #  ← Puede cambiar este valor.

def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

print(f"El factorial de {n} es: {factorial(n)}")