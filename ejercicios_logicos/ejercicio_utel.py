#  Dado un arreglo de enteros no ordenado 'nums', regresa el entero positivo faltante más pequeño. #
#  En caso de necesitar algún algoritmo de ordenamiento deberás implementarlo tú mismo, no usar una función que ordene. #
#  Ejemplo 1: #
#  Input: nums = [1,2,0] #
#  Output: 3 #
#  Explicación: Los números en el rango [1,2] están en el arreglo. #
#  Ejemplo 2: #
#  Input: nums = [3,4,-1,1] #
#  Output: 2 #
#  Explicación: 1 está en el arreglo pero 2 falta.
#ordenar de menor a mayor

numeros = [-2, -2, -2, -1]
def ordenar_ascendente(lista):
    num = len(lista)
    
    for i in range(num):
        
        for j in range(0, num-i-1):
            if lista[j] > lista[j+1]:
                
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


numeros = ordenar_ascendente(numeros)

def num_faltante():
    nueva_lista =[]
    
    for num in numeros:
        if num > 0:
          if num not in nueva_lista:
              nueva_lista.append(num)

    if  not nueva_lista:
      cont =1
      return cont
  
    cont = nueva_lista[0]

    if cont !=1:
        return 1
    for faltante in nueva_lista:

        if faltante != cont:
            return cont
        cont += 1
        
    
    return cont
    
print(f"El numero menor positivo faltante es {num_faltante()}")
