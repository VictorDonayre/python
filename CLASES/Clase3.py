#if 
edad = 18 
if edad >= 18: 
  print("Sos mayor de edad ") 
#if - else 
edad = 17
if edad >= 18:
  print("Sos mayor de edad ") 
else:
  print("Sos menor de edad ") 
#if - elif - else 
nota = 75
if nota >= 90:
  print("Tenes una excelente calificacion")
elif nota >= 80: 
  print("Tenes una buena calificacion")
elif nota >= 70:
  print("Tenes una calificacion regular")
else:
  print("Necesitas mejorar ") 

#DIVISION 
def division(dividendo, divisor):
  if divisor == 0:
    return "Error"
  return dividendo / divisor 
print(division(5,0)) 

#Iterando sonbre una lista 
frutas = ["manzana", "cereza", "banana"]
for fruta in frutas: 
  print(fruta) 

#Iterando usando un rango de numeros
for i in range(5):
  print(i) 

#USANDO EL BUBLE WHILE 
contador = 0
while contador < 5:
  print(contador) 
  contador += 1  

#Ejemplo de Iterador 
class Contador:
  def __init__(self, max):
    self.max = max
    self.n = 0
  def __iter__(self):
    return self 
  def __next__(self):
    if self.n < self.max:
      resultado = self.n
      self.n += 1
      return resultado
    else:
      raise StopIteration
contador = Contador(5) 
for numero in contador:
  print(numero)

#Ejemplo de generador 
def contador(max):
  n = 0
  while n < max:
    yield n 
    n += 1 
  for numero in contador (5):
    print(numero) 

#BREAK 
for i in range(10):
  if i == 5:
    break
  print(i)

#CONTINUE
for i in range(10):
  if i == 5:
    continue 
  print(i)

#PASS 
for i in range(10):
  if i == 3: 
    pass #Este es un marcador de posicion 
  print(i) 

#FOR - ELSE 
for i in range(5):
  if i == 3:
    break
  print(i)
else: 
  print("Bucle terminado sin interrupciones") 

#WHILE - ELSE 
n = 0
while n < 5:
  if n == 3:
    break 
  print(n)
  n += 1 
else:
  print("Bucle terminado sin interrupciones")