numeros = [4,7,1,42,15]

#encontrando el numero más alto
numero_max = max(numeros)
print(f'mayor {numero_max}')

#encontrando el numero más bajo
numero_min = min(numeros)
print(f'menor {numero_min}')

#redondeando un numero con round
numero = 13.2648987
redondeado = round(numero,3)#el ,3 indica los decimales a redondear
print(f'redondeado round {redondeado}')

#retorna false si es : false, 0, None, "", o cualquier valor vacío \ true distinto a 0,caadena no vacia,true
resultado_bool = bool("")
print(f'booleano {resultado_bool}')

#retorna true si todos los datos son verdaderos
resultado_all = all([[1,2],True,"Hola",[1,2]]) 
print(f'resultado all {resultado_all}')

#suma todos los valores de un iterable
suma_total = sum(numeros)
print(f'suma total {suma_total}')