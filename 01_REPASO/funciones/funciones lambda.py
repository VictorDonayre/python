#creando una funcion lambda (anonima) que multiplique por 2 
multiplicar = lambda x : x*2 
print(multiplicar(2)) 
print('--------------------------------------------------------------------------------->')

#creando una funcion que nos diga si el numero es par o no 
numeros = [1,2,3,4,5,6,7,8,9,10]

def es_par (num):
    if num%2==0:
        return True 
#usando filter con una funcion comun 
numeros_pares = filter(es_par,numeros)
print(list(numeros_pares))

print('--------------------------------------------------------------------------------->')

#Haciendo la misma funcion pero con lambda 

numeros_pares2 = filter(lambda numero:numero%2==0, numeros) 
print(list(numeros_pares2)) 
