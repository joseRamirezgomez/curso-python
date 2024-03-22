#creando una lista con list
lista = list([29, False,2,3,4, True])

#devuelve la cantidad de elementos de la lista
resultado = len(lista)

#agregando un elemento con append
#lista.append("jajajajajja")

#agregando un elemento con insert
#lista.insert(2,"que onda?")

#agregando varios elementos
lista.extend([1,True])

#eliminando un elemento por su indice
lista.pop(-1) # -1 para  eliminar el ultimo elemento -2 el antepenultimo ...

#remviendo por su valor
#lista.remove('eso')

#eliminando todod los elemeto
#lista.clear()

#ordena la lista pero con numeros ascendente con reverse=True es descendente
lista.sort()

#invierte los elementos de una lista la revierte asi sea sin ordenaarla de < a > o de mayor a menor
lista.reverse()

print(lista)