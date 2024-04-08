
def ordenar_ascendente(lista):
    n = len(lista)
    
    for i in range(n):
        
        for j in range(0, n-i-1):
            
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

numeros = [5, 2, 8, 1, 9, 3]

print("Lista ordenada:", ordenar_ascendente(numeros))