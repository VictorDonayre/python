#cambiar el tipo de dato de una columna
import pandas as pd 
df = pd.read_csv('01_REPASO\\EJERCICIOS\\problemas_resueltos\\datos.csv') 

#convertir a string los datos de una columna 
df['edad'] = df['edad'].astype(str)
print(type(df['edad'][0]))
print('----------------------------------------------------------------------->')

#reemplazando un valor por otro 
df.replace({'nombre':{'chloe':'maría'}}, inplace = True)
print(df['nombre'])
print('----------------------------------------------------------------------->')

print(df)
print('----------------------------------------------------------------------->')

#eliminando las filas con datos faltantes 
df = df.dropna()
print(df) 
print('----------------------------------------------------------------------->')

#eliminando filas repetidas 
df = df.drop_duplicates() 
print(df) 

#creando un CSV con el dataframe resultante (limpio) 
df.to_csv('01_REPASO\\EJERCICIOS\\problemas_resueltos\\datos_limpios.csv')