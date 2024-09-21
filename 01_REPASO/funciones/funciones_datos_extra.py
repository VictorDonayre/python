#Creando una funcion con varios parametros
def frase (nombre,apellido,adjetivo):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo} seguí así' 

frase_resultante = frase(adjetivo ='inteligente',nombre ='Victor',apellido ='Donayre') 
print(frase_resultante)
print('------------------------------------------------------------------------------------>')

#Creando la misma función con un parámetro opcional y un valor predefinido
def frase (nombre,apellido,adjetivo='Brillante'):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo} seguí así'
frase1 = frase(adjetivo = 'Capo',nombre='Victor',apellido='Donayre') 
print(frase1) 
