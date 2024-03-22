diccionario = {
    "nombre" : 'lucas',
    "apellido" : 'perez',
    "subs" : 100000
}

#devuelve un objeto dict_item
claves = diccionario.keys()

#obtiene un elemento con get(), si no lo encuentra el programa devuelve none y continua
valor_de_apellido = diccionario.get("apellido") 

#eliminando un elemento
diccionario.pop("subs")

#obtiene un elemento dict_itemms iterable
diccionario_iterable = diccionario.items()


#eliminando todo del diccionario
#diccionario.clear()
print(diccionario_iterable)