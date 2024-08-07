#Crear un programa que solicite al usuario un entero y lo imprima por pantalla. 

numero = int(input("Ingrese un numero entero: "))
print("El numero ingreado es: ", numero) 

 #crear un programa que solicite al usuario dos numeros enteros y luego imprima por pantalla: +-*/%

numero_1 = int(input("Ingrese el primer numero: ")) 
numero_2 = int(input("Ingrese el segundo numero:")) 
suma = numero_1 + numero_2 
print("La suma de ambos numeros es: ", suma) 

resta = numero_1 - numero_2 
print("La resta de ambos numeros es: ", resta) 

multiplicacion = numero_1 * numero_2 
print("La multiplicacion de ambos numeros es: ", multiplicacion) 

division = numero_1/numero_2 
print("La division de ambos numeros es: ", division) 

resto = numero_1 % numero_2 
print("El resto de ambos numeros es: ", resto) 

#Crear un programa que solicite al usuario un entero y muestre por pantalla si es par o impar. 

entero = int(input("Ingrese un numero entero: "))
if entero % 2 == 0:
   print("Es par")
else:
   print("Es impar")

#Crear un programa que solicite al usuario su añp de nacimiento y otro año y le diga que edad tenia en el año ingresado. 

año_nacimiento = int(input("Ingrese el año en el que nacio:")) 
año_random = int(input("Ingrese un año cualquiera: "))
edad = año_random - año_nacimiento 
print("Usted tenia ", edad , " años en el año " , año_random)

#Crear un programa que solicite al usuario 5 numeros enteros y el promedio de ellos. 
print("Ingrese 5 numeros enteros: ") 
numero1 = int(input("Ingrese el primer numero: ")) 
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))
numero4 = int(input("Ingrese el cuarto numero: "))
numero5 = int(input("Ingrese el quinto numero: ")) 
suma = (numero1 + numero2 + numero3 + numero4 + numero5)
promedio = suma / 5 
print("El promedio de los numeros ingrasados es: ", promedio) 

#Crear una funcion que reciba un numero y muestre el anterior y el siguiente. 
numero = int(input("Ingrese un numero para saber el anterior y posterior a este: "))
def anterior_posterior(numero):
  print("El numero anterior es: ", numero - 1)
  print("El numero posterior es: ", numero + 1)
anterior_posterior(numero) 

#Crear una funcion que una un string y un entero, ambos dentro de una string. 
print("La union de un string y un entero es: ") 
def union(string, entero):
  print(string, entero) 
union("Numero :", 15) 
#Crear una funcion que reciba un entero y retorne el resto y el cociente. 
print("El resto y el cociente del entero es: ") 
def resultado(numero_1, numero_2):
  print(numero_1 % numero_2) 
  print(numero_1 / numero_2)
  return numero_1 % numero_2, numero_1 / numero_2 
resultado(10, 5) 

#Pedir nombre y apellido por separado e imprimir "Apellido, Nombre". 
nombre = str(input("¿Cual es tu nombre?: ")) 
apellido = str(input("¿cual es tu apellido?: "))
print(f"{nombre}, {apellido}")  

#Obtener una palabra e imprimir la cantidad de letras
palabra = str(input("Ingrese una palabra: "))
print("La cantidad de letras de la palabra es: ", len(palabra)) 

#obtener una palabra e imprimir los primeros 5 caracteres. 
palabra = str(input("Ingrese una palabra: ")) 
print("Los primeros 5 caracteres de la plabra son: ", palabra[:5:]) 

#obtener una palabra, borrarle todas las "a" e imprimirla por pantalla. 
def eliminar_a(palabra):
  palabra_sin_a = palabra.replace("a", "")
  return palabra_sin_a 
palabra = str(input("Ingrese una palabra: "))
resultado = eliminar_a(palabra)
print("Palabra sin la letra a: ", resultado) 
print("solucionado ALEX")