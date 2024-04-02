#parametro args
def suma(nombre,*numeros):# el *numeros lo convierte en una lista
    return f'{nombre}, la suma de tus numeros es {sum(numeros)}'

resultado = suma("jose",1,2,3,4,5,6,7,8,9)
print(resultado)

#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([1,2,3,4,5,6,7,8,9])
print(resultado2)