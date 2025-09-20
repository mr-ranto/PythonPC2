"""
Problema 9:
Escribe un programa que encuentre todos los números perfectos menores que 1000. Un número
perfecto es un número entero positivo que es igual a la suma de sus divisores propios positivos
(excluyendo el propio número).
"""
def encontrar_perfectos(limite=1000):
    #Encuentra números perfectos menores al límite
    perfectos = []
    for numero in range(1, limite):
        suma = 0
        for divisor in range(1, numero):
            if numero % divisor == 0:
                suma += divisor
        if suma == numero:
            perfectos.append(numero)
    return perfectos

# Llamar a la función
perfectos = encontrar_perfectos(1000)
print("Números perfectos < 1000:", perfectos)