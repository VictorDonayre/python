numeros = [1,5,10,15,16,18,25,8,17]

#obteniendo el numero mayor 
numero_mayor = max(numeros)
print(f'el valor maximo es: {numero_mayor}')

#obteniendo el menor valor 
numero_menor = min(numeros)
print(f'el valor minimo es: {numero_menor}')

#sumando los valores
suma_total = sum(numeros) 
print(f'la suma de los valores es: {suma_total}')

#redondeando a 6 decimales 
numero = round(12.345678,2)
print(f'el numero redondeado es: {numero}')

#retorna False -> 0, vacio, False, None / True -> distinto a 0, cadena, datos no vacios 
resultado_bool = bool([1,15,15])
print(resultado_bool)

#retorna True si todos los valores son verdaderos. 
resultado_all = all([1,5,1,51,['hola','adios',15]]) 
print(resultado_all)