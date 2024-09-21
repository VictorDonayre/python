import pygame
from personaje import Cubo
from enemigo import Enemigo
import random   
pygame.init()
 
ANCHO = 1000
ALTO = 500 
VENTANA = pygame.display.set_mode([ANCHO, ALTO])
FPS = 60
FUENTE = pygame.font.SysFont("Comic Sans", 40)  

jugando = True
reloj = pygame.time.Clock() 
tiempo_pasado = 0
tiempo_entre_enemigos = 500 
cubo = Cubo(ANCHO/2,ALTO-60)
enemigos = []
vida = 5 
puntos = 0 
nivel = 1
 
enemigos.append(Enemigo(ANCHO/2, 100))  
def gestionar_teclas(teclas):
    if teclas[pygame.K_a]:
        cubo.x -= cubo.velocidad
    if teclas[pygame.K_d]:
        cubo.x += cubo.velocidad 
while jugando and vida > 0:
    tiempo_pasado += reloj.tick(FPS)
    if tiempo_pasado > tiempo_entre_enemigos:
        enemigos.append(Enemigo(random.randint(0, ANCHO),-100))
        tiempo_pasado = 0 
    eventos = pygame.event.get()
    teclas =  pygame.key.get_pressed()
    texto_vida = FUENTE.render(f"Vidas: {vida}", True, "white")
    texto_puntos = FUENTE.render(f"Puntos: {puntos}", True, "white")
    texto_nivel = FUENTE.render(f"Nivel: {nivel}", True, "white")
     
    gestionar_teclas(teclas) 
    
    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False
    VENTANA.fill("Black")
    cubo.dibujar(VENTANA) 
    for enemigo in enemigos:
        enemigo.dibujar(VENTANA)
        enemigo.movimiento()
        if pygame.Rect.colliderect(cubo.rect, enemigo.rect):
            vida -= 1
            print(f"te quedan {vida}: vidas")
            enemigos.remove(enemigo)
        if enemigo.y + enemigo.alto > ALTO:
            puntos += 1
            enemigos.remove(enemigo)
              
    VENTANA.blit(texto_vida, (20,20))
    VENTANA.blit(texto_puntos, (20,60))
    VENTANA.blit(texto_nivel, (20,110))
           
    pygame.display.update()
    
quit() 
