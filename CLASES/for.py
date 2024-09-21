#Imprimir la tabla del 5 
for i in range (1,13):
    resultado = 5*i
    print(f"5 x {i} es: {resultado}")  

#Sumar los numeros pares del 1 al 20 
suma = 0
for numero in range (1,21):
    if numero %2 == 0:
        suma += numero
        print("La suma de de los pares del 1 al 20 es: ", suma) 

#Contar cuantas veces aparece una letra específica en una palabra dada. 
palabra = "abracadra" 
letra_a_contar = "a"
contador = 0

for letra in palabra:
    if letra == letra_a_contar:
        contador += 1
print(f"La letra {letra_a_contar} aparece {contador} veces en la palabra {palabra}" ) 

#Invertir una cadena de texto 
cadena = "Hola mundo"
cadena_invertida = " " 

for letra in cadena:
    cadena_invertida = letra + cadena_invertida 
print("La cadena invertida es: ", cadena_invertida) 

#Calcular el factorial de un número 
numero = 3
factorial = 1 
for i in range(1, numero + 1):
    factorial *= i 
print(f"El factorial de {numero} es: {factorial}") 

#Crear un triángulo de números 
for i in range (1,6):
    for j in range(1, i + 1):
        print(j, end="") 
    print() 
    
#encuentra el número más grande de una lista 
numeros = [10, 20, 30, 40, 50] 
maximo = numeros[0] 
for numero in numeros:
    if numero > maximo:
        maximo = numero 
print("El número más grande es: ", maximo) 

#imprimir numero impares entre 1 y 30 
for numero in range (1,31): 
    if numero %2 != 0:
        print(numero)  

#Sumar los dígitos de un número 
numero = 123456789
suma_digitos = 0 
for digito in str(numero):
    suma_digitos += int(digito) 
print("La suma de los dígitos del numero es: ", suma_digitos) 

#Generar una secuencia de los cuadrados del 1 al 10 
for i in range (1,11):
    cuadrado = i**2 
    print(f"El cuadrado de {i} es: {cuadrado}") 

#Lista 
nombres = ["Juan","Ana","Julio"] 
print("El tipo de nombre es: ", type(nombres)) 
for nombre in nombres:
    print("Buenos días", nombre) 

#Tuple 
nombres = ("Juan", "Ana", "Julio")
print("El tipo de nombre es: ", type(nombres)) 
for nombre in nombres:
    print("Buenos días: ", nombre) 
     

#Set
nombres ={"Juan","Ana","Julio"} 
print("El tipo de nombre es: ", type(nombres)) 
for nombre in nombres:
    print("Buenos días: ", nombre) 

#Diccionario 
nombres ={"Juan": 1, "Ana":2, "Julio":3} 
print("El tipo de nombre es: ", type(nombres)) 
for nombre in nombres: 
    print("Buenos días: ", nombre, nombres[nombre]) 
     
    