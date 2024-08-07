#escribir la expresion para saber si un numero es mas grande que otro, guardala en una variable de tipo bool e imprimela por pantalla para ver su valor. 
numero_1 = int(input("ingrese un numero: "))
numero_2 = int(input("ingrese otro numero: ")) 
if numero_1 > numero_2:
  print(numero_1, "es mayor que ", numero_2) 
elif numero_1 < numero_2:
  print(numero_1, "es menor que: ", numero_2)
else:
  print(numero_1, "es igual que: ", numero_2)  

#Repetir el punto anterior pero con la expresion que determina que una letra NO es una vocal. 
letra = input("ingrese una letra: ")
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
  print("La letra ", letra , " es una vocal")
else:
  print("No es una vocal") 

#Repetir pero la expresion que permite saber si un numero es par y menor a 10.
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
  if numero < 10: 
    print("El numero es par y menor que 10")
  else: 
    print("El numero es par y mayor que 10")
else:
  print("El numero es impar") 

#ESTRUCTURAS DE CONTROL CONDICIONALES 
#crear una funcion que dado un número, devuelva su valor absoluto. EL valor de un numero es el mismo sin
#considerar el signo.Por ejemplo, el absoluto de 2 es 2 (|2| = 2) y el absoluto de -4 es 4 (|-4|=4).
def valor_absoluto (numero):
  if numero < 0:
    return -numero 
  else:
    return numero 
print(valor_absoluto (-8))
print(valor_absoluto(-5))
print(valor_absoluto(10)) 

#Escribir un codigo que dado dos enteros, determine si la suma de ambos da menos que 100. Si la suma de ambos
#es menor a 100, calcular cuanto falta para llegar a 100 y mostrar por pantalla un mensaje con ese valor.
#Si la suma es mayor a 100, mostrar un mensaje diciendo "Llega a 100".
def suma_menor_limite (num1, num2, limite=100):
  suma = num1 + num2 
  if suma < limite:
    diferencia = limite - suma
    print(f"La suma de {num1} y {num2} es menor que {limite}, falta {diferencia} para {limite}")
  else:
    print(f"La suma de {num1} y {num2} llega a {limite} y es mayor") 
numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))
limite = int(input("Ingrese el limite que desea, por defecto es 100: ")) 
suma_menor_limite(numero_1, numero_2, limite) 

#Se tienen las letras para representar las estaciones del año:
#V para verano, O para otoño, I para invierno y P para primavera 
#Crear una funcion que dada una letra, imprima por pantalla la estacion del año que representa
#Si el usuario escoge otra letra mostrar un mensaje que diga error.
def estaciones_letras ():
  print("¡Hola! podes poner una letra para seleccionar la estación que desees, V para verano, P para primavera, O para otoño e I para invierno: ")
  estaciones = input() 
  if estaciones == "V":
    print("Seleccionaste Verano")
  elif estaciones == "P":
    print("Seleccionaste primavera")
  elif estaciones == "O":
    print("Seleccionaste Otoño")
  elif estaciones == "I":
    print("Seleccionaste Invierno")
  else:
    print("¡Ups! creo que esa estacion no existe")
estaciones_letras() 

#ESTRUCTURAS DE CONTROL ITERATIVAS 
#Se quiere hacer un programa para enseñar a unos niños a contar, Crear una funcion que reciba un numero
#entero e imprima por pantalla los numeros del 1 hasta ese numero con la estructura de control iterativa for.
def numero_entero(): 
  numero = int(input("Eliga un numero: "))
  for i in range(1, numero + 1):
    print(i) 
numero_entero() 

#Se quiere mejorar el programa para enseñar matematica pensando en el ejercicio anterior, ahora se nececita 
#una funcionalidad que permita a los niños aprender las tablas. Crear una funcion que reciba un numero entero 
#y lo imprima por pantalla la tabla de ese numero del 1 al 10.
def tabla(numero): 
  for i in range(1,13):
    resultado = numero * i
    print(f"{numero} multipicado por {i} es igual a {resultado}") 
numero = int(input("Ingrese un numero: ")) 
tabla(numero) 

#Crear una funcion que simule un compleaños, que dado un entero imprima "Que lo cumplas feliz" esa cantidad de veces
def simular_cumpleaños(cantidad_veces):
  for i in range(cantidad_veces):
    print("Feliz cumpleaños") 
veces = int(input("Ingrese la cantidad de veces que desea escuchar feliz cumplaños: "))
simular_cumpleaños(veces)

#En un almacén están buscando la forma de hacer los cobros más automaticamente para esto se nos pide crear una
#función que reciba un numero entero que representa lo que hay que cobrar, le pida al usuario ingrear un monto
#y se vaya mostrando por pantalla cuanto falta para completar el pago. Repetir este proceso hasta que la deuda
#sea 0 o menor. 
def realizar_cobro(total_a_pagar):
  deuda_restante = total_a_pagar 
  while deuda_restante > 0:
    print(f"\nDeuda restante: ${deuda_restante:.2f}")
    pago = float(input("Ingrese monto a pagar: $ "))

    if pago <= 0:
      print("Por favor ingrese un monto válido que sea mayor a 0") 
      continue 
    deuda_restante -= pago
    if deuda_restante < 0:
        print(f"Pago recibido restan ${deuda_restante:.2f} para saldar la deuda")
    elif deuda_restante > 0:
      print(f"Pago recibido, el pago excedió la deuda por: ${-deuda_restante:.2f}") 
print("La deuda ha sido saldada") 
monto_total = float(input("Ingrese monto total a cobrar: $")) 

realizar_cobro(monto_total) 

#Escribir código que recorra los números del 1 al 20 y determine para cada uno si es par o impar, imprimiendo un mensaje por pantalla en cada caso.
def par_impar(numero):
  if numero % 2 == 0:
    print(f"El numero, {numero} es par") 
  else:
    print(f"El numero {numero} es impar") 
for numero in range(1,21):
  par_impar(numero) 

#Se tiene una máquina de sacar juguetes que funciona cuando se ingresa una determinada cantidad de fichas,
#y se quiere hacer una funcion que imite ese comportamiento.
# A) Hacer una funcion que reciba un numero que represente el precio de la máquina, e imprima por pantalla
# "ingresá x fichas para comenzar" hasta que se hayan ingresado esa cantidad de letras F (que representan
# una ficha) y luego ¡A jugar! cuando se hayan ingresado todas las fichas necesarias.
def empezar_juego(canti_fichas):
  fichas_ingresadas = 0
  while(fichas_ingresadas<canti_fichas):
    fichas_restantes = canti_fichas - fichas_ingresadas
    print(f"Ingresá {fichas_restantes} para comenzar") 
    letras = input() 
    if letras == "F":
      fichas_ingresadas += 1
      print(f"¡Ficha aceptada! has ingresado {fichas_ingresadas} de {canti_fichas}") 
    else: 
      print(f"Entrada no válida por favor ingrese fichas F para poder jugar")
empezar_juego(3) 
print("¡A jugar!") 

#Crear una funcion que reciba un número entero e imprima los numeros primos entre 0 y el número ingresado.
def es_primo(n):
  if n <= 1:
    return False
  if n <=3:
    return True 
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n %(n+2) == 0:
      return False 
    i +=6 
    return True 
def imprimir_num_primo(limite):
  print(f"Números primos entre 0 y {limite} son: ")
  for numero in range(2, limite + 1):
    if es_primo(numero):
      print(numero, end = " ") 
print() 
limite = int(input("Ingrese un numero entero: ")) 
imprimir_num_primo(limite) 
    



