"""
Problema 11:
Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
por ejemplo, omitiendo las vocales.
Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
minúsculas.
"""

texto = input("Ingrese texto: ")
resultado = ""
for letra in texto:
    if letra.lower() not in "aeiou":  # Convertir a minúscula para comparar
        resultado += letra
print("Texto sin vocales:", resultado)