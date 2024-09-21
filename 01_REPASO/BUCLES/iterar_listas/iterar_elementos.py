animales = ['perro', 'gato', 'loro', 'cocodrilo'] #cramos una lista 
numeros = [1,15,12,19]
#recorriendo lista de animales 
for animal in animales: #por animal (creamos una nueva variable) en animales (el bucle recorre cada elemento de nuestra lista)
    print(f'Ahora la variable animal es: {animal}') 
#imprimimos animales, se imprimira nuestra lista cuantos valores tenga, esto nos tiene que devolver
#perro, gato, loro, cocodrilo 
print("-----------------------------------------------------------------")
#recorriendo lista de numeros y multiplicando por 10 
for numero in numeros:
    resultado = numero * 10 
    print(f'el numero {numero} x 10 = {resultado}')
print("-----------------------------------------------------------------")

#iterando con dos listas del mismo tamaño al mismo tiempo con zip()
for indice, (numero,animal) in enumerate(zip(numeros,animales)): #Usamos enumerate para obtener el indice luego zip para emparejar el valor de ambas listas 
    print(f'El indicie de ambas listas es: {indice}')
    print(f'El valor de la lista 1 es: {numero}')
    print(f'El valor de la lista 2 es: {animal}')
print("-----------------------------------------------------------------")

#forma no optima de recorrer una lista con su indice (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
print("-----------------------------------------------------------------")

#forma optima de recorrer una lista con su indice 
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El indice es: {indice} y el valor es: {valor}') 

print("-----------------------------------------------------------------")
#usando el ese
for numero in numeros:
    print(f'Ejecutando el último bucle, valor actual: {numero}') 
else:
    print('bucle terminado')

#Todo lo anterior funciona exactamente igual con tuplas y conjuntos 

