#Crear una lista con los numeros del 1 al 10. 
#Acceder a la posicion que contiene el numero 5 e imprimirlo por pantalla 

lista_numero1 = list(range(1,11))
print(lista_numero1[4])
 
#con la lista del punto anterior, usar la funcion len para averiguar su longitud e imprimirla. 
print(len(lista_numero1))

#Crear seceuncia con números distintos, y luego devolver el elemento maximo y minimo 
numeros = [5, 8, 10, 85, 15, 10, 1, 20, 26 ]
print(numeros)

print("Lista ordena de forma creciente: ") #ordenada de forma creciente (Ej. 4)
numeros.sort() 
print(numeros)

print("Lista ordenada en forma decreciente: ") 
numeros.sort(reverse = True)
print(numeros)

numero_maximo = numeros[0]
for num in numeros:
    if num > numero_maximo:
        numero_maximo = num 
print("El valor máximo de la lista es: ", numero_maximo)

numero_minimo = numeros [0]
for num in numeros:
    if num < numero_minimo:
        numero_minimo = num 
print("El valor mínimo de la lista es: ", numero_minimo) 

#Hacer una funcion que reciba una lista y devuelva un string uniendo las palabras desde el final de la lista hasta el
#principio con un " " (espacio) entre cada una para formar una frase. 

frases = [ 
            "entender", "pueden", "humanos", "los", "que", "código", "escriben", "programadores", "buenos", "Los", 
            "entiende.", "computadora", "una", "que", "código", "escribe", "tonto", "Cualquier"
            ]

def frase (frases):
    oracion = ""
    frases.reverse() 
    oracion = " ".join(frases) 
    return oracion 

oracion = frase(frases)
print(oracion)

#hacer una función que reciba dos strings, un string y un substring, es decir que el primero contiene al segundo 
#se pide devolver el string habiendo eliminado el substring del mismo 

frase1 = "Pensamiento Computacional 2024 Computacional" 
palabra1 = "Computacional" 

def eliminar (string, substring):
    if not substring in string:
        return string
    string = string.replace(substring, " ") 
    return string 
resultado = eliminar(frase1, palabra1)  
print(resultado) 

#Manuel y su pareja armaron una lsita con las tareas del hogar, decidieron dividirse la lista, al Manuel le tocó hacer
#todas las actividades con número par, hacer una función que reciba una lista de enteros, y devuelva otra con numeros pares

lista_numeros = [1, 2, 5, 4, 9, 10, 12, 45, 18, 14, 48, 19, 18, 14] 

def es_par(numero):
    if numero % 2 == 0:
        return True 
    return False   
    
def enteros(lista):
    num_par = []
    for numero in lista:
        if es_par(numero) and not numero in num_par: 
            num_par.append(numero) 
    return num_par 
lista_numeros_pares = enteros(lista_numeros) 
print(lista_numeros_pares)  

#crear una tupla que guarde tu nombre y edad. Luego, imprimir por pantalla tu edad, accediendo al elemento de la tupla

mi_nombre = ("Victor", 19 )
edad = mi_nombre[1] 
print(f"Mi edad es: {edad}") 

#Hacer una lista con 5 nombres, y realizar las siguientes actividades con la misma: 
# a) cambiar el ultimo elemento de la lista y cambiar el último nombre por "Juan". olvidándonos de que sabemos que tiene
#5 elementos ¿Cómo podriamos saber el último elemento si no sé cuál es la longitud? 
# b) Devolver el nombre que esté a dos posiciones del final. ¿Cómo haremos para que nos funcione para cualquier lista
#y no solo a los que tienen 5 elementos 
# c) Recorrer la lista e imprimir cada nombre por pantalla
# d) imprimir por pantalla la lista con 3 repeticiones, usar el operador repetición * 

lista_nombres = ["Pedro", "Mateo", "Sofia", "Daniel", "Ethan"] 
lista_nombres [-1] = "Juan" #-1 accede al último elemento de la lista independientemente de la longitud 
ultimo_elemento = lista_nombres[-1] 
print(f"El ultimo elemento de la lista es: {ultimo_elemento}") 

#podemos usar los indices negativos para acceder a los elementos que estan al final y posterior a este 
elemento_dos_posiciones = lista_nombres[-3] # -3 indica que nos moveremos 3 posiciones desde el ultimo elemento 
print(f"El nombre que está a dos posiciones del final es:  {elemento_dos_posiciones}") 
#recorremos e imprimimos la lista 
for nombre in lista_nombres:
    print(nombre)
#imprimimos la lista 3 veces 
print(lista_nombres * 3) 

#Se pide ahora crear 3 tuplas con un nombre y edad, luego guardarlas en una lista. 

nombre1 = ("Mateo", 19) 
nombre2 = ("Ethan", 15) 
nombre3 = ("Angel", 20) 

personas = [nombre1, nombre2, nombre3] 

print(personas) 

#EJERCICOS CON LSITAS Y TUPLAS 

#Se quiere guardar información de los siguientes países: Francia, Argentina, Japón, Alemania, Perú.
# a. crear una tupla para cada país que contenga su nombre, capital y su continente donde se encuentra. 
francia = ("Francia", "Paris", "Europa") 
argentina = ("Argentina", "Buenos Aires", "Sudamérica") 
japon = ("Japón", "Tokyo", "Asia") 
alemania = ("Alemania", "Berlin", "Europa") 
peru = ("Perú", "Lima", "Sudamérica")

#b. Guardar las tuplas en una lista 

paises = [francia, argentina, japon, alemania, peru] 

#c. Hacer una función que reciba por parámetros la lista, e imprima la información de cada país. 

def informacion_pais(lista_paises): 
    for pais in lista_paises:
        nombre, capital, continente = pais 
        print(f"País: {nombre}")
        print(f"Capital: {capital}")
        print(f"Continente: {continente}") 
informacion_pais(paises) 

#Una libreria tiene un sistema que guarda los nombres de todos los libros que tienen en una lista, se quiere saber
#cuántos libros tienen repetidos. hacer un código que imprima para cada título, cuántos ejemplares hay. 
from collections import Counter #Es una clase de módulo que facilita el conteo de una lista. 

lista_libros = ["el principito", "it", "más allá del jardín", "a través de mi ventana", "it"
                "cincuenta sombras liberadas", "el principito", "it", "padre rico, padre pobre", "a traves de mi ventana"
                "cincuenta sombras liberadas", "romeo y julieta"]
contar_libros = Counter(lista_libros) 
for libros, cantidad  in contar_libros.items(): 
    print(f"Título: {libros}, Cantidad de libros: {cantidad}")  

#Crear una lista que contenga los números del 1 al 10, luego recorrela y guardar en otra lista elevado al cuadrado

lista1 = list(range(1,11))
print("Numeros del 1 al 10 elevados al cuadrado") 
for num in lista1:  
    print(num **2) 
    
# Crear un programa donde el alumno ingrese las materias que va haciendo, donde pueda almacenarlas hasta que ingrese
#una "X" 
 
def guardar_materias (): 
    materias = [] #Creamos una lista vacia para almacenar los datos ingresados por el usuario
    
    while True: #Cramos un bucle 
        materia = input("Ingrese las materias que desee almacenar o 'X' para terminar: ")
        if materia.upper() == 'X': #comparamos con X, usamos upper ya que convierte a mayúsculas 
            break # si la condicion es verdadera se rompe el bucle al ingrear "X"
        materias.append(materia) #añadimos cada elemento a nuestra lista 
    return materias # nos devuelve la lista de materias 
lista_materias = guardar_materias() #creamos otra variable donde almacenaremos la función 
print("Materias guardadas: ") 
for materia in lista_materias:
    print(materia) #imprimimos la lista de materias

#se tiene un ticket de supermercado que se puede representar como una lista de tuplas, producto y precio.
#Hacer una funcion que reciba la lista, calcule y devuelva el total que hay que pagar. 
def calcular_total(ticket):
    total = sum(precio for _, precio in ticket)
    return total
ticket =[("Jabón", 15), ("Papel", 20), ("Dentrífico", 18), ("Leche", 16)] 
print("La lista es: ", ticket)
total = calcular_total(ticket) 
print(f"Total a pagar del ticket: {total}") 

#Ahora se tienen dos tickets. Juntar ambos y volver a calcular el total 

def combinar_ticket(ticket1, ticket2):
    ticket_combinado = ticket1 + ticket2
    return calcular_total(ticket_combinado)
ticket1 = [("Jabón", 15), ("Papel", 20), ("Dentrífico", 18), ("Leche", 16)] 
ticket2 = [("Manzana", 20), ("Detergente", 15.5), ("Shampoo", 25), ("Carne", 18)] 
total_combinado = combinar_ticket(ticket1, ticket2)
print(f"La suma de ambos tickets es: {total_combinado}") 
