with open ('01_REPASO\\archivos\\texto.txt', 'a', encoding = 'UTF-8') as archivo:
    
    archivo.write('\n')
    #usando un bucle para agregar varias lineas
    
    for i in range (5): archivo.write(f'Linea {i+1} agregada! \n')