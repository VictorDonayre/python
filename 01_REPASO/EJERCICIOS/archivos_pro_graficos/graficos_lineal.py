import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv('01_REPASO\\EJERCICIOS\\archivos_pro_graficos\\datos_gases.csv') 

#creando el gráfico lineal  
sns.lineplot(x="fecha",y="gases",data=df) 

plt.show() 
