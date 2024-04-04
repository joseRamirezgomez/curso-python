with open("archivo\\texto.txt","w",encoding="utf-8")as archivo:
    #sobreescribiendo el archivo
    #archivo.write("jajajajajajaj")
    
    #agregando 2 lineas on writelines
    archivo.writelines(["hola\n","que onda?\n"])
    
    #agregando otras 2 lineas on writelines
    archivo.writelines(["hola\n","que onda?\n"])