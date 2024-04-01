frutas = ["pera","chirimoya","chulupa", "guayaba","manzana"]
cadena = "hola soy jose"
numeros = [1,4,6,3,2]
#evitando comer pera con sentencia continue
print("----------saltando el bucle con continue-------------")

for fruta  in frutas:
    if  fruta == "manzana":
        continue
    print(f'me como una {fruta}')

#evitar que el bucle siga ejecutando con break y el else tampoco se ejecuta
print("----------deteniendo el bucle con break-------------")

for fruta in frutas:
    print(f'me voy a comer una {fruta}')
    
    if fruta == "guayaba":
        break

print('fin del bucle')

#recorrer una cadena de texto
print("----------recorre una cadena de texto-------------")
for caracter in cadena:
    print(caracter)
print("----------------------------")
#for en una sola linea duplicando numeros
numeros_duplicados =[x*2 for x in numeros]
print(numeros_duplicados)