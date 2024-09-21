#si el modulo se encontrara en una carpeta de la misma ruta se inporta así 
#import funciones_buenas.saludar as m_saludar

import sys 
sys.path.append('d:\\GIT\\python\\Funciones_buenas')

import saludar as saludo
print(saludo.saludar("Victor"))

