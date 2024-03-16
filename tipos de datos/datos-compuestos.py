#una lista se puede modificar
lista = ["Jose DEV", "Soy DEV", True, 1.75]
#tupla es similar  a una lista pero no se puede cambiar los valores
tupla = ("Jose DEV", "Soy DEV", True, 1.75)
#metodo de modificar  una lista
lista[0] = "José" 
print(lista[0])
# creando un conjunto (set)
# al igual que la tupla no se puede modificar los elementos pero si redefinir y no repite datos
conjunto = {"Jose DEV", "Soy DEV", True, 1.75}

#creando un diccionario (dict)
diccionario = {
    'nombre' : "Jose DEV",
    'canal' : "Soy Dev",
    'estado' : True,
    'altura' : 1.74,
    'dato_duplicado' : "Soy Dev" 
}

print(diccionario['altura']+ 2)