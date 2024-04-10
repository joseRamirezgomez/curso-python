import pandas as pd

#usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv("archivo\\datos.csv")
df2 = pd.read_csv("archivo\\datos.csv")


#obteniendo los datos  de las columnas "Nombre"
nombre = df["nombre"]

#ordnando el dataframe por la edad
#ordenanado de forma ascendente
df_ordenado = df.sort_values("edad")

#ordenando de forma descendente
df_ordenado_descendente = df.sort_values("edad",ascending=False)

#contatenando los 2 dataframes
df_concatenado = pd.concat([df,df2])

#accede a las primeras filas con head()
primer_fila = df.head(2)

#accede a las ultimas filas con
ultima_fila = df.tail(2)

#obteniendo el total de filas y columnas con shape
filas_y_columnas = df.shape

#desmpaquetando las filas y columnas con shape
filas,columnas = df.shape

#obteniendo data estdistica del dataframe
df_info = df.describe()

#accediendo al elemento especifico con loc
elemento_especifico = df.loc[2,"edad"]

#accediendo a un elemento con iloc
elemento_especifico_iloc = df.iloc[2,2]

#accediendo a los apellidos con loc
apellidos_loc = df.loc[:,"apellido"]

#accediendo al apellido con iloc 
apellidos_iloc = df.iloc[:,1]

#accediendo a los datos de la fila 2 con loc
fila_2 = df.loc[2,:]

#accediendo a los datos de la fila 2 con iloc
fila_2_iloc = df.iloc[2,:]

print(fila_2_iloc)
  