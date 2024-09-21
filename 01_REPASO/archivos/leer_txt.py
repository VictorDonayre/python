#usando open para abrir un archivo con una codificacion universal (UTF-8)
archivo_sin_leer = open("01_REPASO\\archivos\\texto.txt", encoding = 'UTF-8') 

#Leer archivo completo
#archivo = archivo_sin_leer.read()

#leer linea por linea  
#lineas = archivo_sin_leer.readlines() 

#leer una sola linea 
linea = archivo_sin_leer.readline()

#cerramos el archivo con close 
archivo_sin_leer.close

print(linea) 


 