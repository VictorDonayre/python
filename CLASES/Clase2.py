#RECIBE 2 NUMEROS Y DEVUELVE LA SUMA DE ELLOS 
nombre = str((input("Ingrese su nombre: "))) 
print("¡Hola! " + nombre + " Voy a pedirte que ingreses dos numeros")
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
suma = numero1 + numero2 
print("La suma de ambos numeros es: " + str(suma)) 

#RECIBE EL NOMBRE DE UNA PERSONA Y SALUDA 
def saludar (nombre):
 print("Hola " + nombre + " espero que estes muy bien") 

saludar("Matthew")

#RECIBE 2 NUMEROS Y DEVUELVE LA SUMA DE ELLOS 
def suma (sumando_1, sumando_2):
  resultado = sumando_1 + sumando_2 
  return resultado
resultado_suma = suma(5, 8)
print(resultado_suma)
resultado_suma = suma(21, 8)
print(resultado_suma)

#RECIBE 2 NUMEROS Y DEVUELVE LA SUMA Y RESTA DE ELLOS
def resultados (numero_1, numero_2):
  suma = numero_1 + numero_2 
  resta = numero_1 - numero_2
  return suma, resta 
suma, resta = resultados(8, 13)
print("La suma es: " , suma)
print("La resta es: " , resta) 
