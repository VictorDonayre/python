cadena1 = 'Hola,Compa,Como,Estas'
cadena2 = 'bienvenidos' 

#devuelve el resulado en minuscula
minusc = cadena1.lower()  

#devuelve el resultado en minuscula 
mayusc = cadena1.upper()

#Convierte solamente la primera letra a mayuscula 
capi = cadena1.capitalize() 

#buscamos una cadena en otra cadena, si no encuentra un valor o coincidencias nos devuelve -1 (no existe) 
find = cadena1.find(" ") 

#buscamos una cadena en otra cadena, si no encuetra un valor o coincidencias lanza una excepción 
index = cadena1.index("a")

#si es numérico devuelve True ya sea una cadena de texto, de lo contrario devuelve False 
es_numerico = cadena1.isnumeric()

#si es alfanumerico devuelve True solo si no tiene caracteres especiales, de lo contrario devuelve False 
es_alfa = cadena1.isalpha() 

#contamos las coincidencias de una cadena dentro de otra cadena, devuelve la candidad de coincidencias encontradas
count = cadena1.count("a")

#contamos cuantos caracteres tiene una cadena 
len = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es así devuelve True
comienza_con = cadena1.startswith("t")

#verificamos si una cadena termina con otra cadena dada, si es así devuelve True 
termina_con = cadena1.endswith("hola")

#si el valor 1 se encuentra dentro de la cadena original, reemplaza el valor 1 de la misma, por el valor 2 
nueva_cadena = cadena1.replace(",", " ")
nueva_cadena2 = nueva_cadena.capitalize() 

#separar cadenas con las cadenas que le pasemos
separar_cadena = cadena1.split(",")

print(separar_cadena)
