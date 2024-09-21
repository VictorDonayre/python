#Crear una función que nos devuelva los números primos entre 0 y el argumento que le pasamos 

#Creando una funcion que verifique si el numero es primo 
def es_primo(numero):
    #Verificamos que el numero pasado no pueda dividirse por ningun numero entre 2 y el mismo numero -1
    for i in range(2,numero-1):
        #Si es divisible por alguno retornamos false y termina el blucle 
        if numero%i == 0: return False 
    #Si termina el bucle, significa que no fue divisible por lo tanto es primo 
    return True 

#creando funcion que retorne una lista con todos los numeros primos 
def primos_hasta(numero):
    #creamos la lista 
    primos = [] 
    for i in range(2,numero+1):
        #verificamos si el valor es primo 
        resultado = es_primo(i)
        #En caso de que sea primo lo agregamos a la lista 
        if resultado == True: primos.append(i) 
    #devolvemos la lista
    return primos

#creamos el resultado y llamamos a la función
resultado = primos_hasta(13) 

#Mostrando el resultado 
print(resultado)