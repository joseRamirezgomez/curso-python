animales = ["gato", "perro", "loro","cocodrilo"]
numeros = [1,55,33,62]

#recorriendo lista animales
for animal in animales:
    print(f'El animal es : {animal}')
    
#recorriendo lista de numeros y multiplicando por 10
for numero in numeros:
    resultado = numero*10
    print(resultado)
    
print("------------------------")
#interando 2 listas del mismo tamaño al mismo tiempo
for numero,animal in zip(numeros,animales):
    print(f'lista 1: {numero}')
    print(f'lista 2: {animal}')

print('---------------------------')
#forma correcta de de recorrer una lista con su indice
for num in  enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es {indice} y el valor {valor}')

#usando el for/else
print('------------------------')
for num in numeros:
    print(f'ejecutando el bucle numero actual: {num}')
else:
    print('terminado el bucle')

#todo lo anterior funciona exactamente igual para tuplas y conjuntos