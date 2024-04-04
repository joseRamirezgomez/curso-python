#abriendo un archivo con with open
with open("archivo\\texto.txt",encoding="utf-8")as archivo: 
    #lee el archvo
    contenido = archivo.read()
    
    #mostrando el archivo
    print(contenido)
    
#NO ES NECESARIO CERRAR EL ARCHIVO CON WITH, PORQUE SE CIERRA AUTOMATICAMENTE