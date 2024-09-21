#2 listas una con nombre y otra con apellido 
nombres = ['Lucas','Nicolas','Chloe','Matthew','Daniel'] 
apellidos = ['Dalto','Dotti','Decker','Ramos','Olivencia'] 

#Registrando esta información en un txt de forma optima 
with open('01_REPASO\\EJERCICIOS\\problemas_resueltos\\nombres_y_apellidos.txt', 'w', encoding='UTF-8') as arch:
    arch.writelines('Los datos son: \n\n') 
    [arch.writelines(f'Nombres: {n}\nApellido {a}\n ------------------------\n') for n,a in zip(nombres,apellidos)] 
    
    