#crando un conjunto con set ()
conjunto = set(['data1', 'data2']) 

#creando un conjunto dentro de otro conjunto usando forzenset 
conjunto1 = frozenset(['data1', 'data2','data3'])
conjunto2 = {conjunto1, 'data4'} 

#teoria de conjuntos 
conjuntoa = {1,3,5,7,9}
conjuntob = {1,3,5,7,9}

#verificando si es un subconjunto 
resultado1 = conjuntob.issubset(conjuntoa)
resultado2 = conjuntob <= conjuntoa 

#verificando si es un superconjunto 
resultado3 = conjuntoa.issuperset(conjuntob) 
resultado4 = conjuntoa > conjuntob 

#verificando si hay algun elemento en comun 
resultado5 = conjuntoa.isdisjoint(conjuntob) 

print(resultado4) 

 