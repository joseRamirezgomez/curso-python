#2 listas, una con nombres y otra con apellidos
nombres = ["jose","estephania", "maria","alejandro","natalia", "luis"]
apellidos = ["rodriguez","ramirez","gonzales","ortiz","lopez","garcia"]

#registra la informacion en un txt de forma optima
#con "with open("archivos_problemas_resueltos\\nombres_apellidos.txt","w") as arch:" 
#se puede crear  el archivo si no existe o agregar a uno que ya existe

with open("archivos_problemas_resueltos\\nombres_apellidos.txt","w") as arch:
  arch.writelines("los datos son: \n\n")
  [arch.writelines(f'Nombre: {n}\n Apellido: {a}\n ---------------\n') for n,a in zip(nombres,apellidos)]
  