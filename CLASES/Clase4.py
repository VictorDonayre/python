#SECUENCIAS, TUPLAS Y LISTAS. 
#TUPLAS 
def edad(persona):
    return(persona[1])
personas = [
    ("Juan" , 25), ("Sergio", 20), ("Nataniel", 26), ("Mateo", 19) 
            ]
personas.sort(key=edad, reverse = True)
personas.remove(("Sergio", 20))
personas.append(("Guillermo", 30))
personas.insert(3, ("Mario", 22))
print(personas)
print("\n")
print("Filtrado y transformación de secuencias") 
#FILTRADO Y TRANSFORMACION DE SECUENCIAS 
def cortar_palabra(palabra):
    return palabra[:4]
palabras = (
    "mesa", "silla", "ventana", "puerta", "auto", "pileta", "plantas"
)
palabras_cortas = map(cortar_palabra, palabras) 
print(list(palabras_cortas)) 

#Otro ejemplo:
def sumar (numero):
    return numero + 1
numeros = [1, 2, 5 , 6, 9, 8, 10, 15]
nuevos_numeros = list(map(sumar, numeros)) 
print(nuevos_numeros) 
print("\n")
print("Filter")

def palabras_cortas(palabra):
    longitud = len(palabra)
    if longitud < 5:
        return True 
    else:
        return False 
palabras = (
    "mesa", "silla", "ventana", "puerta", "auto", "pileta", "plantas"
)

palabra_corta = filter(palabras_cortas, palabras)
print(list(palabra_corta))  

