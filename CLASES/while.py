#Escribe un programa que cuente del 1 al 5 
print("Contar del 1 al 5: ")
numero = 0
while numero <5:
    numero += 1 
    print(numero) 
    
#Escribe un programa que sume todos los numeros del 1 al 10.
print("Suma de los numeros del 1 al 10: ") 
suma = 0
numero = 1 
while numero <=10: 
    suma += numero 
    numero += 1 
print(f"La suma de los numeros del 1 al 10 es: {suma}") 

#Crea un juego simple donde el usuario debe de adiviar un numero entre 1 y 10 
import random 
numero_secreto = random.randint(1,10) 
adivinanza = None 
print("¡Bienvenido al juego!")
print("Estoy penzando en un número entre el 1 y el 10, ¿Podés adivinar cúal es el número?") 
while adivinanza != numero_secreto:
    adivinanza = int(input("Escoge un número: ")) 
    if adivinanza < numero_secreto:
        print("El número es muy bajo seguí intentando") 
    elif adivinanza > numero_secreto: 
        print("El número es muy alto seguí intentando")
    else:
        print("¡Felicidades, adivinaste el número!") 
print("Gracias por jugar, nos vemos en otro juego") 

#Factorial de un numero 
numero = int(input("Ingresa un numero para saber su factorial: ")) 
factorial = 1 
contador = numero 
while contador > 0:
    factorial *= contador 
    contador -= 1 
print(f"El factorial de {numero} es: {factorial}") 

