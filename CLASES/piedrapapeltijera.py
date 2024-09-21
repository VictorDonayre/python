#Crear un programa donde sea imposible ganar en "piedra, papel o tijera" 
def jugar ():
    print("¡JUGUEMOS! Ingresa R para piedra, P para papel y T para tijera") 
    jugada = input() 
    if jugada == "R": 
        print("PAPEL")
        print("Perdiste") 
    elif jugada == "P":
        print("TIJERA")
        print("Perdiste")
    elif jugada == "T":
        print("PIEDRA") 
        print("Perdiste")
    else:
        print("Por favor escoge una de las opciones")
        print("Perdiste")
jugar()

