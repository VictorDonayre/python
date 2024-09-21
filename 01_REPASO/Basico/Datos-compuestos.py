#creamos una lista (se puede modificar) 
lista = ["Ignacio", "Omar", "Mario", True, 15] 
#Creamos una tupla (no se puede modificar) 
tupla = ("Ignacio", "Omar", "Mario", True, 15) 

#modificamos la lista 
lista [1] = "Daniel" #Esto es válido 

#tupla[1] = "Daniel" -> Esto no es válido

#print(lista) # reemplazamos a "Omar" por "Daniel" 

#Creando un conjunto (set) (No se accede a los elementos a partir del índice, no almacena datos duplicados ) 
conjunto = {"Ignacio", "Omar", "Mario", True, 15} 
#print(conjunto[3]) -> No se puede acceder al elemento. 
 
#Creando un diccionario(dict) (la estructura es key:value separamos con ",") 
diccionario = {
    'nombre':'victor',
    'edad':19,
    'está_aprendiendo_a_programar': True,
    'dato duplicado':'victor'
} 
print(diccionario['nombre']) 
