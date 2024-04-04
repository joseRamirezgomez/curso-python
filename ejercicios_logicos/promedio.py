#pide 3 numeros al usuario y calcula el promedio

#numero1 =float(input("ingresa un numero "))
#numero2 =float(input("ingresa un numero "))
#numero3 =float(input("ingresa un numero "))

#promedio =  (numero1 + numero2 + numero3)/3

#print(f'el promedio de {numero1}, {numero2}, {numero3} es {promedio}')

#optimizando 
def  calcular_promedio():
    numeros = []
    for i in  range(3):
        num = float(input(f"Ingrese el {i+1}o. numero: "))
        numeros.append(num)
    
    promedio =sum(numeros)/3
    print(f"Tu promedio es de: {promedio}")
    
calcular_promedio()