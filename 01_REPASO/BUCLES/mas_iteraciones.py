frutas = ['banana','manzana','pera','frutilla','mango']
cadena = 'Hola Mundo'
numeros = [2,5,8,10]

#saltandonos una iteracion con la sentencia continue 
for fruta in frutas:
    if fruta == "mango":
        continue
    print(f'Me voy a comer una: {fruta}')
print('------------------------------------------------------------------------>')

#terminando una iteracion con la sentecia break (el 'else' tampoco se ejecuta)
for fruta in frutas:
    if fruta == "frutilla":
        break #el bucle se rompre cuando llega a frutilla 
    print(f'Me voy a comer una: {fruta}')
else:
    print('Bucle terminado')
print('------------------------------------------------------------------------>')

#recorrer una cadena de texto 
for letra in cadena:
    print(letra)

#ultilizando for en una sola linea de codigo 
numeros_duplicados = [x*2 for x in numeros] #por x en numeros multiplica x por 2 [4,10,16,20]
print(numeros_duplicados)