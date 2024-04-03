
idioma = input("selecciona ing si tu idiomas es ingles o es si es español ")

#manejo de modulos para cambiar de idioma (experimento)
def español():
    #importa todo el  modulo y lo guarda en una variable llamada saludo_español
    import modulo_saludar as saludo_español

    saludo = saludo_español.saludar("jose")
    print(saludo)
    
def ingles():
    #importa solo la función que se llama
    #para importar un modulo dentro de una carpeta se utiliza
    from idiomas.ingles import saludar
    saludo = saludar("jose")
    print(saludo)
    
if idioma == "es":
    español()
elif idioma == "ing":
    ingles()
