#creando un conjunto con set()
conjunto = set(["Dalto1", "Dalto2"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato3"}

print(conjunto2)

#teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,5}

#verificacion si es un sub cconjunto
resultado = conjunto2.issubset(conjunto1)  #devuelve True si todos los elementos de conjunto2 están en conjunto1
resultado = conjunto2 <= conjunto1 
print(resultado) 

#verifica si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)  
resultado = conjunto2 > conjunto1 
print(resultado) 

#verifica si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)