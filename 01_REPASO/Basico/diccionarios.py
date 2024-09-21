#creando diccionario con dict()
diccionario = dict(nombre = 'victor', apellido = 'donayre') 

#las listas no pueden ser claves y usamos frozenset para meter conjuntos 
diccionario = {frozenset(['aprendiendo ' 'a']): 'programar'} 

#creando un diccionario con fromkeys() valor por defecto None 
diccionario = dict.fromkeys(['nombre','apellido','carrera'])

#creando un diccionario con fromkeys() cambiando el valor a "Sin dato" 
diccionario = dict.fromkeys(['nombre','apellido'], 'Sin Dato')

print(diccionario)