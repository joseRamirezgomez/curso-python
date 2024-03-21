cadena1 = "hola,Como,Estas"
cadena2 = "holaeso"

#print(dir(cadena1)) #muestra todos los metodos de la clase

#convertir a mayuscula
mayus =  cadena1.upper() 

#convertir a minuscula
minusc = cadena1.lower()

#convierte primera en mayuscula
prime_mayus = cadena1.capitalize()

#buscar una cadena en otra cadena si no hay coinsidencia vuelve -1
busqueda_find = cadena1.find("s")

#buscar una cadena en otra cadena si no hay coincidencias lanza una execpcion
busqueda_index = cadena1.index("a")

#si es numerico devuelve true
es_numerico = cadena2.isnumeric()


#si es alphanumerico devuelve true son todas las letras de la a-z sin espacios
es_alphanumerico = cadena2.isalpha()

#buscar una cadena en otra cadena devuelve la cantidad de coincidencias
coicidencia = cadena1.count('h')

#cuenta cuantos caracteres tiene una cadena
longitud = len(cadena1)

#verifica si una cadena empieza con una cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith('hola')

#verifica si una cadena termina con una cadena dada, si es asi devuelve true
termina_con = cadena1.endswith('Estas')

#remplaza una palabra por otra en una cadena
cadena_nueva =  cadena1.replace(',', ' ')

#separa cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")

print(cadena_separada[1])