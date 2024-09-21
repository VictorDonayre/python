diccionario ={
    "Nombre" : 'Victor',
    "Apellido": 'Donayre',
    "Edad" : 19 
}

#Nos devuelve un objeto dict_item (podemos iterar) 
claves = diccionario.keys() 

#Obtener un elemento del dict (si no lo encuentra nos lanza None osea no existe)
buscando_item_Edad = diccionario.get("Edad")

#Eliminando todo el diccionario 
#diccionario.clear()

#Eliminando un elemento del diccionario
diccionario.pop("Edad")

#obteniendo un elemento dict_items iterable 
diccionario_iterable = diccionario.items()

print(diccionario_iterable)

