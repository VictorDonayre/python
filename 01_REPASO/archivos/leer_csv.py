import csv
with open('01_REPASO\\archivos\\datos.csv') as archivo_csv:
    reader = csv.reader(archivo_csv) 
    for row in reader:
        print(row) 
         