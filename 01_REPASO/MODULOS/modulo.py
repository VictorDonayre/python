#Importando un modulo y asignandole el nombre "m_saludar" 
# import saludar as m_saludar 

#Desde ese modulo importamos dos funciones y cambiamos el nombre 
from Funciones_buenas.saludar import saludar as saludo_1 ,salu2 as saludo_2 #ponemos el nombre de la carpeta "." y el nombre del modulo 
saludo = saludo_1("Matthew") 
saludo2 = saludo_2("Daniel")

#mostrando los resultados 
print(saludo)
print(saludo2)

#para ver las propiedades y metodos de el namespace 
#print(dir(m_saludar))

#accedemos al nombre de este modulo 
print(__name__) 

#accedemos al nombre del modulo llamado 
#print(m_saludar.__name__) 

