"""
Problema 12:
Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en
la lista abajo:
[
"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto",
"Septiembre", "Octubre", "Noviembre", "Diciembre"
]
Luego, genere esa misma fecha en formato AAAA-MM-DD.
"""

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

fecha = input("Ingrese fecha (ej: 9/8/1636 o Septiembre 8, 1636): ").strip()

if "/" in fecha:
    # Formato MM/DD/AAAA
    partes = fecha.split("/")
    if len(partes) == 3:
        mes = int(partes[0])
        dia = int(partes[1])
        año = partes[2]
    else:
        print("Formato numérico inválido")
        exit()
else:
    # Formato textual
    partes = fecha.split()
    if len(partes) >= 3:
        mes_nombre = partes[0]
        dia = int(partes[1].strip(","))
        año = partes[2]
        # Buscar mes en la lista
        mes_encontrado = None
        for i, m in enumerate(meses):
            if m.lower() == mes_nombre.lower():
                mes_encontrado = i + 1
                break
        if mes_encontrado:
            mes = mes_encontrado
        else:
            print("Mes no válido")
            exit()
    else:
        print("Formato textual inválido")
        exit()

# Formatear con ceros a la izquierda
print(f"{año}-{mes:02d}-{dia:02d}")