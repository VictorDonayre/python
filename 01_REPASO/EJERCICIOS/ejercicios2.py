#Faltó el prfesor y los alumnos harán su propia clase 
#profesor
#asistente 
#A) pedir el nombre y la edad de los compañeros que vinieron hoy a clase y ordenar los datos de mayor a menor 
#B) el mayor de la clase es el profesor y el menor el asistente 

#Pedir el nombre y la edad de los alumnos 
def obtener_alumnos(cantidad_alumnos):
    #Creando una lista vacía 
    alumnos = [] 
    
    #Creando un bucle for para pedir información de cada alumno 
    for i in range (cantidad_alumnos):
        nombre = str(input('Ingrese el nombre del alumno: ')) 
        edad = int(input('Ingrese la edad del alumno: ')) 
        alumno = (nombre, edad)
        
        #agregando información en la lista
        alumnos.append(alumno)
        
    #ordenando de menor a mayor según la edad
    alumnos.sort(key=lambda x:x[1]) 
    
    #alumnos[x] devuelve una tupla con (nombre, edad) y luego accedemos al nombre y edad para definir al profesor y asistente 
    asistente = alumnos[0][0] 
    profesor = alumnos [-1][0] 
    
    #retornamos la tupla
    return asistente, profesor 

#desempaquetamos y llamamos a la función 
asistente, profesor = obtener_alumnos(5) 

#mostramos el resultado
print(f'El profesor es: {profesor} y su asistente es {asistente}') 
 
    