#Diferencia en porcentaje entre el curso actual y el más rapido de otros cursos 

#Datos 
otro_curso_maximo = 7
otro_curso_minimo = 2.5
otro_curso_promedio = 4
curso_dalto = 1.5 

#Diferencias de crudos 
crudo_promedio = 5
crudo_dalto = 3.5

#Diferencias de duracion
diferencias_con_min = round((1- curso_dalto / otro_curso_minimo) * 100,1)
diferencias_con_max = round((1- curso_dalto / otro_curso_maximo) * 100,1)
diferencias_con_prom = round((1- curso_dalto / otro_curso_promedio) * 100,1)

#calculamos el espacio vacio de tiempo removido 
tiempo_vacio_promedio = round((1- otro_curso_promedio / crudo_promedio) * 100,1) 
tiempo_vacio_dalto = round((1 - curso_dalto / crudo_dalto) * 100,1)
print("----------------------------------------------------------------------------->")
#Calculamos la diferencias de duracion (Ejercicio a)
print (f'El curso de Dalto dura un {diferencias_con_min}% menos que el curso más rápido')
print (f'El curso de Dalto dura un {diferencias_con_max}% menos que el curso más lento') 
print (f'El curso de Dalto dura un {diferencias_con_prom}% menos que el promedio')

print("----------------------------------------------------------------------------->")

#calculamos la cantidad de espacios vacios que se remueven (Ejercicio b) 
print(f'El promedio de espacios vacios que remueven otros cursos es del {tiempo_vacio_promedio}%') 
print(f'Este curso elimina un {tiempo_vacio_dalto}% de tiempo vacío') 

print("----------------------------------------------------------------------------->")
#mostrando diferencias entre curso si duraran 10 horas (Ejercico C)
print(f'Ver 10 horas del curso de Dalto equivale a ver {round((otro_curso_promedio / curso_dalto)* 10,1)} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {round((otro_curso_promedio / curso_dalto) *10,1)} horas de otros cursos')
