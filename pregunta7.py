"""
Problema 7:
Escribe un programa que encuentre la suma de todos los números primos menores que 100.
"""
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

suma = 0
for numero in range(2, 100):
    if es_primo(numero):
        suma += numero

print("Suma de los números primos menores a 100:", suma)