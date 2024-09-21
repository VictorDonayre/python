diccionario = dict(nombre = 'victor', apellido = 'donayre', edad = 19)

#recorriendo el diccionario y obteniendo la clave 
for key in diccionario.items():
    key
    print(f'La clave es: {key}')
print('------------------------------------------------------------------------------------')

#recorriendo el diccionario con .items() para obtener la clave y el valor 
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'La clave es: {key}, El valor es: {value}')