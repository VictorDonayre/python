with open ('01_REPASO\\archivos\\texto.txt', 'w', encoding = 'UTF-8') as archivo:
    
    #Sobreescribiendo el archivo 
    #archivo.write('Texto cambiado')  
    
    #escribiendo dos lineas 
    archivo.writelines(["Mirá pá estoy apendiendo a", " programar en", ' Python\n' ])
    
    #escribiendo otras dos lineas 
    archivo.writelines(["Este es mi primera vez sobreescribiendo un txt"])