#Pedirle al usuario que escribra una palabra
texto_real = input('Escriba una palabra y calcularemos cuantos tardarías en decirlo: ')
cantidad_de_palabras = texto_real.split(" ") 
total_palabras = len(cantidad_de_palabras) 
print(f'Dijiste {total_palabras} palabras y tardarías {total_palabras/2} segundos en decirla') 
print(f'Dalto tardaría {total_palabras/2*1.3} segundos') 
if total_palabras > 120:
    print("Tampoco te pedí que escribieras un testamento")
 