archivo_sin_leer = open("archivo\\texto.txt",encoding="utf-8")

#leer un archivo completo
#archivo = archivo_sin_leer.read()

#leer linea por linea
#lineas = archivo_sin_leer.readlines()

#leer una sola linea
linea = archivo_sin_leer.readline()#si se agrega un numero en () lee esa cantidad de caracteres

#cierra el archivo 
archivo_sin_leer.close()

print(linea)