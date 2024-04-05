#pide al usuario un texto y cuenta la cantidad de vocales

frase = input("ingresa una frase ").lower()
contador = 0
for letra in frase:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contador+= 1

print(f'la frase tiene {contador} vocales')