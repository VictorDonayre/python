#crando una funcion simple 
def saludar():
    print("Hola,¿cómo estás?") 
saludar()
print('------------------------------------------------------------------>') 

def saludar (nombre,sexo):
    sexo = sexo.lower() 
    if (sexo == 'mujer'):
        adjetivo = 'reina' 
    elif (sexo == 'hombre'):
        adjetivo = 'titan' 
    else:
        adjetivo = 'amor' 
    print(f'Hola! {nombre}, mi ¡{adjetivo}! ¿Cómo estás') 
saludar('Carl','')
print('------------------------------------------------------------------>') 

#crear una funcion que nos retorne multiples valores 
def crear_contraseña_random(num):
    chars = "abcdefghij" 
    num_entero = str(num)
    num = int(num_entero[0]) 
    c1 = num - 2
    c2 = num
    c3 = num - 5 
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}' 
    return contraseña,num

#Desempaquetando la función 
password,primer_numero = crear_contraseña_random(18) 

#Mostrando los datos obtenidos y los datos utilizados para obtenerlo 
print(f'Tu contraseña nueva es: {password}')
print(f'El numero ultilizado para crearla fue: {primer_numero}')