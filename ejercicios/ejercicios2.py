#el profesor falto a clases los alumnos deben de hacer de profesor el mayor y asistente el menor
C = int(input("¿Cuantos estudiantes asistieron hoy? "))
def rol_clase(cantidad_estudiante):
    estudiantes = []
    for i in range(cantidad_estudiante):
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        estudiante=(nombre,edad)
        estudiantes.append(estudiante)
    estudiantes.sort(key=lambda x:x[1])
    asistente= estudiantes[0][0]
    profesor = estudiantes[-1][0] 
    return asistente,profesor

asistente,profesor = rol_clase(C)

print(f'El profesor es: {profesor} y el asistente es: {asistente}')