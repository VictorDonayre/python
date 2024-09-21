#creando una lista con lis() 
lista = list([19, 20, 30, 25, 80, 15]) 

#devuelve la cantidad de elementos de una lista 
cantidad_elemtos = len(lista)

#agregamos un elemento a la lista con append 
lista.append(16)

#agregando un elemento a la lista desde un índice específico
lista.insert(2, 11)

#agregamos una lista dentro de otra lista 
lista.extend([2032])

#eliminamos un elemento de la lista a partir de su indice 
lista.pop(-1) #-1 eliminamos el ultimo elemento de la lista, -2 eliminados el penultimo elemento de la lista y asi sucesivamente

#removemos un elemento de la lista por su valor 
lista.remove(19)

#Eliminamos todos los elementos de una lista 
#lista.clear() 

#Ordenamos una lista de fomra ascendente (revere=True para ordenar de forma descentente)
#lista.sort()

#Invirtiendo una lista con reverse (funciona para cualquier lista) 
lista.reverse()
print(lista) 
