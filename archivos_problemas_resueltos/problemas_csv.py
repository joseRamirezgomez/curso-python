import pandas as pd

df = pd.read_csv("archivos_problemas_resueltos\\datos.csv")

#convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str) 

#mostrar el tipo del dato
#print(type(df['edad'][0])) 

#remplazando los datos mendez por boomerang
df['apellido'].replace('Mendez',"Boomerang",inplace=True)

print(df)
print("---------------------------")

#elimina filas con datos faltantes
df = df.dropna()

#eliminando filas con datos duplicados
df = df.drop_duplicates()

#creando un csvcon dataframe resultante (limpio)
df.to_csv("archivos_problemas_resueltos\\datos_limpios.csv")