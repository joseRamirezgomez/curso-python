#el profesor falto a clases los alumnos deben de hacer de profesor el mayor y asistente el menor
C = int(input("¿Cuantos estudiantes asistieron hoy? "))

#funcion para obteneral asistente y al profesor segun la edad
def rol_clase(cantidad_estudiante):
    estudiantes = []
    #ejecutando un for pra info de los estudiantes
    for i in range(cantidad_estudiante):
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        estudiante=(nombre,edad)
        
        #agregando la informacion a la lista
        estudiantes.append(estudiante)
    #ordena de menor a mayor * edad
    estudiantes.sort(key=lambda x:x[1])
    asistente= estudiantes[0][0]
    profesor = estudiantes[-1][0] 
    return asistente,profesor

asistente,profesor = rol_clase(C)

print(f'El profesor es: {profesor} y el asistente es: {asistente}')