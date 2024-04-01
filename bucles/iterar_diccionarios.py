diccionario = {
    "nombre": "Jose",
    "apellido": "Ramirez",
    "subs": 100000
}

#recorre el dict para obtener las claves 
for key in diccionario:
    print(f'la clave es: {key}' )


#recorre el dict con items()para obtener claves y valores
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es: {key}, y el valor es: {value}")