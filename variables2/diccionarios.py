#creando un diccionario con dic()
diccionario = dict(nombre="lucas",apellido="perez")

#las listas no pueden ser claves y usamos frozenset  para que sean inmutables.
diccionario = { frozenset(["dalto","viejo"]): "eso"}

#creando diccionarios con fromkeys
diccionario = dict.fromkeys(["nombre","apellido"])


print(diccionario)