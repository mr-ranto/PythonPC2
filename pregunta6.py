"""
Problema 6:
Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
materias.
Puede usar el siguiente esquema a manera de ejemplo
{
Alumno: Juan,
Notas: [10, 12, 15]
}
Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
completo de los alumnos.
"""

alumnos = []
n = int(input("¿Cuántos alumnos desea registrar?: "))

for i in range(n):
    nombre = input(f"Nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Nota {j+1} de {nombre}: "))
        notas.append(nota)
    
    alumno = {"Alumno": nombre, "Notas": notas}
    alumnos.append(alumno)

# Mostrar resultados
print("\n--- LISTADO COMPLETO ---\n")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")