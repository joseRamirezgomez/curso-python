# busca el numero mayor que se repita mas veces
from collections import Counter

def numero_mas_repetido(lista):
    # Contar la frecuencia de cada número en la lista
    conteo = Counter(lista)
    max_repetido = max(conteo, key=lambda x: (conteo[x], x))
    return max_repetido

lista = [1,1,1,2,2]
print("El número más grande que se repite en la lista", lista, "es:", numero_mas_repetido(lista))
