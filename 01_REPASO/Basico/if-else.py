contraseña_base_de_datos = "MichiFuu"
contraseña_ingresada = '''MichiFuu''' 

if contraseña_base_de_datos == contraseña_ingresada:
    print("Inciando sesión...") 
else:
    print("Contraseña incorrecta, intente nuevamente.") 

#ELSE IF que en python (Elif)

ingreso_mesual = 10000
gatos_mensual = 11000
if ingreso_mesual >= 5000:
    if ingreso_mesual - gatos_mensual < 0:
        print("Estás en déficit")
    elif ingreso_mesual - gatos_mensual > 3000:
        print("Estás bien, económicamente") 
    else:
        print("Estás gastando más de lo que ganás")  
elif ingreso_mesual < 5000:
    print("Estás bien en Latinoamérica")
else:
    print("Sos pobre") 

