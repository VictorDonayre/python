#Hacer una funcion que reciba un string que imprima solamente los caracteres que sean vocales. 
def solo_vocales (voc):
    vocales = "aeiouAEIOU" 
    resultado =[caracter for caracter in voc if caracter in vocales] 
    print("".join(resultado)) 
solo_vocales("hola")

#Hacer una función que reciba un string y lo invierta. 
def invertir (pal):
    return pal[::-1] #empieza desde el ultimo elemento de la cadena 
txt = "Hola Mundo" 
txt_invertido = invertir(txt) 
print(txt_invertido) 

#Hacer una funcion que reciba dos strigs, un string y un substring, se pide devolver el stirng habiendo elminado el substring 
frase= "Campeones del mundo - 2022 "
palabra = "2022"
def eliminar (string, substring):
    if not substring in string:
        return string
    string = string.replace(substring, "")
    return string 
resultado = eliminar(frase,palabra) 
print(resultado)

#Un chef esta armando una lista, quiere agregar un ingrediente si no lo escribió antes así no tiene repetidos.
#Hacer un programa que inserte un nuevo elemento siempre y cuando este no este en la lista. 

def agregar_ingrediente(ingredientes, ingrediente_nuevo):
    if ingrediente_nuevo not in ingredientes:
        ingredientes.append(ingrediente_nuevo) 
    return ingredientes 

lista_ingredientes = ["cebolla", "papa", "huevo", "tomate", "leche"]
ingredientes = agregar_ingrediente(lista_ingredientes, "calabaza") #agragamos un nuevo ingrediente 
print(lista_ingredientes) 
ingredientes = agregar_ingrediente(lista_ingredientes, "papa") #verificamos que el programa funcione que no agregue elementos repetidos
print(ingredientes) 

#si se tiene una lista de enteros ordenadadas de mayor a menor. Hacer una funcion que según esta lista inserte un nuevo
#entero, manteniendo el orden.

def agregar_carta(carta, nueva_carta):
    for i in range(len(carta)): #recorremos la lista de cartas 
        if nueva_carta <= carta[i]: 
            carta.insert(i, nueva_carta)
            return carta 
    carta.append(nueva_carta)
    return carta 
carta =[1,4,6,8]
nueva_carta = 5

cartas_actualizadas = agregar_carta(carta,nueva_carta) 
print(cartas_actualizadas) 

#Santiago armó una lista con el pedido de empanadas de su familia pero ahora quiere saber la cantidad de gustos diferentes
#que tiene que pedir.

def contar_gustos_diferentes(lista_empanadas):
    gustos_diferentes = set(lista_empanadas) #set elimina elementos duplicados lo que facilita el conteo de duplicados
    return len(gustos_diferentes) 
lista_empanadas = ["pollo", "jamon y queso", "pollo", "carne","jamon y queso"] 
cantidad_gustos = contar_gustos_diferentes(lista_empanadas)
print(cantidad_gustos) 
  
#Un matrimonio está organizando una fiesta y tiene que armar una lista de invitados. Cada uno tiene su propia
#tupla y guarda en ella a todos los que quiere invitar.
#Si alguien cancela tienen que sacarlo de la tupla.
#Hacer una función que reciba la tupla y un nombre, y devuelva una nueva tupla sin el nombre pasado
#por parámetro.

def eliminar_invidatos(tupla_invitados, nombre): #definimos una funcion para las tuplas
    lista_invitados = list(tupla_invitados) #ingreamos las tuplas en una lista
    if nombre in lista_invitados:
        lista_invitados.remove(nombre) 
    nueva_tupla_invitados = tuple(lista_invitados)
    return nueva_tupla_invitados

invitados = [("Juan"), ("Alex"), ("Ben"), ("Esteban"), ("Daniel"), ("Julian"), ("Maria"), ("Sofia"), ("Ethan")]
nombre_a_eliminar = "Daniel" 

nueva_lista_invitados = eliminar_invidatos(invitados, nombre_a_eliminar) 
print(nueva_lista_invitados) 

#Cuando ya tienen a todos los invitados tienen que juntar sus tuplas, para eso se necesita una función
#que a partir de dos tuplas cree una sola que sea la combinación de ambas tuplas.

def nueva_tupla(tupla1, tupla2):
    tupla_combinada = tupla1 + tupla2 
    return tupla_combinada 

invitados1 = ("Ana", "Sofia", "Luis", "Pedro", "Ethan")
invitados2 = ("Juan", "Omar", "Jean") 

tupla_combinada = nueva_tupla(invitados1, invitados2)
print(tupla_combinada) 
