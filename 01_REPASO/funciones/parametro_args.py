#Forma no optima de sumar valores 
print('---------------------------------------------------->') 
def suma(lista):
    numeros_sumados = 0 
    for numero in lista:
        numeros_sumados = numeros_sumados + numero 
    return numeros_sumados
resultado = suma([5,6,7,8,10,15,20,9]) 
print (resultado)  

print('---------------------------------------------------->') 
#forma optima de sumar valores 
def suma_total(numeros):
    return sum([*numeros]) 
resultado2 = suma_total([5,6,7,8,10,15,20,9,5])
print(resultado2)
print('---------------------------------------------------->') 

#Lo mismo que arriba pero utilizando el operador * como parametro (*args) 
def suma(nombre, *num): #el * transfora los valores a una lista si queremos agragarle más parametros el * tiene que ir al final 
    return f'{nombre}, la suma de tus números es: {sum(num)}'  
resultado = suma('Victor',5,6,7,8,10,15,20,9) 
print(resultado) 