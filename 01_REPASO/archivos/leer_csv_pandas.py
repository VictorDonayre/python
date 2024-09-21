import pandas as pd 

#usando la función read_csv para leer un archivo CSV 
df  = pd.read_csv('01_REPASO\\archivos\\datos.csv', encoding='UTF-8')
df2  = pd.read_csv('01_REPASO\\archivos\\datos.csv', encoding='UTF-8')

#obteniendo los datos de la columna nombre 
nombres = df['nombre']

#ordenando el dataframe por edad forma ascendente 
df_ordenado = df.sort_values("edad") 

#ordenando el daraframe de forma descendente 
df_descendente = df.sort_values("edad", ascending=False)

#concatenando los dos datasframes 
df_concatenado = pd.concat([df, df2]) 

#accediendo a las 2 primeras filas  con head() 
primer_fila = df.head(2)

#accediendo a las 2 ultimas filas con tail()
ultima_fila = df.tail(2)

#accediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape #desempaquetamos para que nos muestre las filas y columnas 

#obteniendo data estadística del dataframe: 
df_info = df.describe()  

#accediendo a un elemto específico del df con loc 
elemento_especifico = df.loc[1,"nombre"] 

#accediendo al nombre de la fila 1 (0 es el indice) con iloc: 
elemento_especifico_iloc = df.iloc[1,0] 

#accediendo a todos las filas de una columna 
nombres = df.iloc[:,0]

#accediendo a los nombres con iloc 
fila1= df.iloc[0,:]

#accediendo a la fila con edad mayor que 
fila_mayor = df.loc[df['edad']>15,:]
print(fila_mayor)

