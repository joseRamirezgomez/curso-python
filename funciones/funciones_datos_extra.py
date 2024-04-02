#funcion de 3 parametros
def frase(nombre,apellido,argumento):
    return f'Hola {nombre} {apellido}, eres muy {argumento}'

frase_final = frase(nombre="juan",apellido="perez", argumento="amazing")
print(frase_final)

#creando la misma funcion con un parametro opcional y valor por defecto
def frase_f(nombre,apellido,argumento="perezoso"):
    return f'Hola {nombre} {apellido}, eres muy {argumento}'

frase_final_f = frase_f(nombre="juan",apellido="perez", argumento="listo")
print(frase_final_f)
