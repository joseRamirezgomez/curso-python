nombre = input("ingresa tu nombre: ")
mujeres = ["camila", "ana", "maria"]
hombres = ["juan", "pedro", "jose"]

for masculino,femenino in zip(hombres, mujeres):
    nombre = nombre.lower()
    if nombre == masculino:
        adjetivo= "bienvenido"
        break
    elif nombre == femenino:
        adjetivo="bienvenida"
        break
    else:
        adjetivo= "bienvenid@"
    
def saludar():
    print(f"salut {nombre} {adjetivo}  a este programa")
    
saludar()

#encriptador ejercicico
def contraseña_random(num):
    chars = 'abcdefghijklmnopqr'
    numero_entero = str(num)
    num =  int(numero_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num + 2
    c4 = num *3
    c5 = num -5
    contraseña = f'{chars[c1]}{chars[c2]}{num*3}{chars[c3]}{chars[c4]}{chars[c5]}'
    return contraseña

password = contraseña_random(input("Ingrese un número entero para generar una contraseña aleatoria: "))
print(f"Tu contraseña es: {password}")