#Escribe un programa que pida al usuario un número y determine si es par o impar
numero = int(input("Ingrese un numero: "))
if numero %2 == 0:
    print(f"El numero {numero} es par") 
else:
    print(f"El numero {numero} es impar") 

#Escribe un programa que reciba 3 numeros del usuario e imprima cual es el mayor.
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: ")) 
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3
print(f"El numero mayor es: {mayor}") 

#Escribe un programa que pida una calificacion entre 0 y 100 e imprima "aprobado" si es mayor o igual a 60 y 
#Reprobrado en caso contario
calificacion = float(input("Ingrese su calificación: ")) 
if calificacion >= 90:
    print("Excelente Calificación, aprobaste con AD") 
elif calificacion >= 80:
    print("Buena calificación, aprobaste con A")
elif calificacion >= 70:
    print("Podes seguir mejorando, aprobaste con B")
elif calificacion >= 60:
    print("Necesitas mejorar, sacaste una C") 
else:
    print("Tenes que esforzarte más, reprobaste F") 

#Escribe un programa que reciba un numero del 1 al 7 e imprima el día de la semana correspondiente.
dia_semana = int(input("Ingrese un número del 1 al 7 para seleccionar el día correspondiente:  "))
if dia_semana == 1:
    print("El día que seleccionó es Lunes")
elif dia_semana == 2:
    print("El día que seleccionó es Martes") 
elif dia_semana == 3:
    print("El día que seleccionó es Miércoles")
elif dia_semana == 4:
    print("El día que seleccionó es Jueves")
elif dia_semana == 5:
    print("El día que seleccionó es Viernes") 
elif dia_semana == 6:
    print("El día que seleccionó es Sábado")
elif dia_semana == 7:
    print("El día que seleccionó es Domingo")
else:
    print("Número inválido")

#Escribe un programa que reciba la edad de una persona y clasifíquela como niño, adolescente, adulto o anciano
edad = int(input("Por favor ingrese su edad: ")) 
if edad <= 12:
    print("Sos niño")
elif edad <= 19:
    print("Sos adolescente")
elif edad <= 59:
    print("Sos adulto") 
else:
    print("Sos anciano") 

#Escribe un programa que pida un número entero positvo y calcule la suma de todos los numeros desde el 1
#hasta ese numero.
numero = int(input("Ingrese un numero entero positivo: ")) 
if numero > 0:
    suma = 0
    for i in range(1, numero + 1): 
        suma += i 
    print(f"La suma de los números desde el 1 hasta el {numero} es: {suma}")
else:
    print("El numero ingresado no es positivo") 
    




