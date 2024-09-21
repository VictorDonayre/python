#Abriendo el archivo con with open 
with open('01_REPASO\\archivos\\texto.txt', encoding = 'UTF-8') as archivo_sin_leer:
    #leemos el archivo 
    contenido = archivo_sin_leer.read() 
    
    #mostramos el archivo 
    print(contenido) 
    
#no es necesario cerrar el archivo al usar with open 