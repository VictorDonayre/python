#SUCESION FIBONZACCI 
print("SUCESION FIBONZACCI")
def fibonacci_iterativo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fib = [0,1]
    for i in range (2,n):
        fib.append(fib[i-1] + fib[i-2])
    return fib
n = 10 
resultado =fibonacci_iterativo(n)
print(f"Los primeros {n} números de Fibonacci son: {resultado} ") 
print("\n")
#LISTAS 
print("LISTAS")
mi_lista = [1,2,3, "Hola", [4,5,6] ] 
#MODIFICAR ELEMENTOS 
mi_lista[1] = "nuevo valor"

#AÑADIR ELEMENTOS 
mi_lista.append ("Nuevo elemento")
#ELIMINAR ELEMTOS  
mi_lista.remove("Hola") 
print(mi_lista)

#TUPLAS 
#USANDO PARÉNTESIS 
print("TUPLAS: ")  
print("Usando paréntesis: ")
mi_tupla = (1,2,3,"Hola", True) 
print(mi_tupla) 
print("\n") 
print("Sin usar paréntesis: ") 
mi_tupla_2 = 1,2,3,"Hola",True
print(mi_tupla_2) 
print("\n") 

#ACCESO A ELEMENTOS
print("ACCESO A ELEMENTOS: ") 
print(mi_tupla[0])
print(mi_tupla[3]) 
print("\n") 

#DESEMPAQUETADO DE TUPLAS
print("DESEMPAQUETADO DE TUPLAS: ") 
a,b,c,d,e = mi_tupla 
print(a)
print(d)
print("\n") 

#OPERACIONES COMUNES CON TUPLAS
print("LONGITUD DE LA TUPLA: ") 
print(len(mi_tupla))  

print("CONCATENACION DE TUPLAS: ") 
nueva_tupla = mi_tupla + (4,5,6)
print(nueva_tupla)  

print("REPETIR ELEMENTOS") 
print(mi_tupla*3) #Repite 3 veces la tupla
print("\n")

#MOSTRAREMOS UN USO PRÁCTICO DE TUPLAS PARA GENERALIZAR LA CONSTRUCCION DE MENÚS DE OPCIONES 
#MEJORAMOS EL PROGRAMA PONIENDOLE PRECIOS A CADA ARTICULO 
def menu(opciones):
    print("Seleciona una opción: ") 
    for i in range (1,len(opciones)):
        print(f"{i} - {opciones[i][0]} ${opciones[i][1]}") 
    opc = int(input())
    while opc not in range (1,len(opciones)):
        opc = int(input())
    return opc
quesos = (" ",("cheddar: ", 75), 
          (" danbo: ", 60), 
          (" Sin queso: ", 0))
panes = (" ", ("árabe: ", 70), 
         (" pebete: ", 60), 
         (" francés: ", 50)) 
carnes = (" ", ("hamburguesa: ", 200), 
          (" jamón crudo: ", 150), 
          (" jamón cocido: ", 140), 
          (" lomito: ", 150), 
          (" salchicha: ", 100), 
          (" veggie: ", 0))
sand=[]
print("Armá tu sandwich: ")
op1=menu(panes)
sand.append(panes[op1][1])
op2=menu(carnes)
sand.append(carnes[op2][1])
op3=menu(quesos)
sand.append(quesos[op3][1])
print("Tu pedido de sandwich de pan ", panes[op1][0], " Saldrá pronto")
print("Detalle: ", carnes[op2][0], quesos[op3][0], sep="\n")
print("Abonar: $%.2f "%sum(sand))


#RANGE 
print("Range Fin: ")
print(list(range (11)))
print("\n")

print("Range Inicio, Fin: ") 
print(list(range (1,11)))
print("\n") 

print("Range Inicio, Fin, Paso")
print(list(range(10,20,2))) 
print("\n") 

#EJEMPLOS 
#¿Cómo cargamos una lista de datos ingresados por le usuario? ¿Cómo mostramos el contenido de una lista? 

#Ej. de carga de impresión de listas
print("Pedirle al usuario que ingrese un nombre y lo devuelve en una lista: ")
nombres = [] 
nom=input("ingrese un nombre (ingrese * para salir: )") 
while nom != "*":
    nombres.append(nom) 
    nom=input("ingrese un nombre (ingrese * para salir: )") 
print("Listas de Nombres: ")
print(nombres) 
print("Salida detallada")
for n in nombres:
    print(n)
print("\n")
#CONSIDERANDO QUE LAS LISTAS SON SECUENCIAS PODEMOS USAR SÓLO PARTES DE ELLAS, POR EJEMPLO, PARA UN FOR 
#Ej. con Listas, con un FOR como una parte de la lista 
print("Genera una lista de 10 números aleatorios entre 1 y 35: ")
from random import randint 
a = [] 
for i in range (20):
    a.append(randint(1,35))
print("Segunda mitad: ")
for n in a[10:]:
    print(n,end=" ") 
print()
print("Primera mitad: ") 
for n in a[:10]:
    print(n,end=" ") 
print() #En este caso creamos una lista de 20 números generados aleatoriamente entre 1 y 35, y utilizamos el for para imprmir los primeros 10 números de la lista. 

