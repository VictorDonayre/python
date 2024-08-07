#Ejercicios con for y while 
print("Ejemplo FOR")
for i in range (5):
    print("Sacar una pelota") 
    
print("Ejemplo WHILE") 
tamaño_globo = 0
while tamaño_globo < 5: 
    print("Inflar globo") 
    tamaño_globo +=1 
#Ejercicios usando for.
#CONTAR HASTA 10 USANDO FOR 
print("Contaremos del 1 al 10: ")
for i in range (1, 11):
    print(i) 
#Sumando numeros hasta 50 usando while 
print("Sumaremos los numeros hasta 50: ") 
suma = 0
numero = 1 
while suma < 50:
    suma += numero 
    print("Suma actual: ", suma)
    numero +=1 
#Repetir una palabra usando FOR 
for i in range(5):
    print("Hola") 

#Usa un bucle while para seguir pidiendo un numero hasta que el usuario adivine cual es el número 
#correcto 
numero_correcto = 8
adivina = int(input("Adivina el número: ")) 
while adivina != numero_correcto:
    print("¡Ups! número incorrecto seguí intentando: ") 
    adivina = (int(input("Adivina el número: "))) 
print("¡Genial! adivinaste el número, el número era", numero_correcto) 

#Contar hacia atrás usando FOR 
for i in range (10, 0, -1):
    print(i)




    