"""
Problema 9:
Escribe un programa que encuentre todos los números perfectos menores que 1000. Un número
perfecto es un número entero positivo que es igual a la suma de sus divisores propios positivos
(excluyendo el propio número).
"""
print("Los números perfectos menores que 1000:")

for numero in range(1, 1000):
    suma_divisores = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma_divisores += divisor
    
    if suma_divisores == numero:
        print(numero, "es perfecto ✅")