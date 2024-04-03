#creando una función que ue devuelva
#numeros primos entre 0 y n numeros

#funcion  para verificar si un numero es primo
def es_primo(num):
    #verifica si en num no divida por 2 y ese mismo numero -1
    for i in range(2,num-1):
        #si es divisible por alguno retorna falso y termina el bucle
        if num%i==0: return False
    #si termina el bucle significa que no fue divisible y es primo
    return True

#funcion lista primos
def primos_hasta(num):
    primos=[]
    for i  in range(2,num+1):
        #verifica si el valor es primo
        resultado = es_primo(i)
        #en caso que sea lo agregamos a la lista
        if resultado == True: primos.append(i)
    return primos

resultado =  primos_hasta(50)
print(resultado)