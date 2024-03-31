#le pedimos al usuario una frase (o varias)
frase = input("Di una frase y te calculo cuanto tardas en decirlas: ")

#creamos una lista con todas las palabras de la frase (se separa cada vez que haya un espacio)
palabras_separadas = frase.split(" ")

#usamos len()para la cantidad de elementos de la lista
cant_palabras = len(palabras_separadas)

#en casos que se tarde mas de un minuto en decirlo, le decimos que pare un poco
if cant_palabras > 120:
    print('pero no te pedi un testamento')

#calculamos cuanro se tarda en decir las palabras    
print(f'dijiste {cant_palabras} palabras, y tardarias {cant_palabras/2} segundos en decirlo')
print(f' dalto lo diria en {cant_palabras *100 // 2 *1.3 /100} segundos')
