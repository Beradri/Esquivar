import pygame
from pygame.locals import *
import sys
import time
import random

# Inicializamos Pygame
pygame.init()

# Configuración de la pantalla
ancho_pantalla = 1920
alto_pantalla = 1080
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

# Cargar imágenes
fondo = pygame.image.load("fondo.png").convert_alpha()
coras0 = pygame.image.load("corazones_0.png").convert_alpha()
coras1 = pygame.image.load("corazones_1.png").convert_alpha()
coras2 = pygame.image.load("corazones_2.png").convert_alpha()
coras3 = pygame.image.load("corazones_3.png").convert_alpha()
objeto1 = pygame.image.load("objeto_1.png").convert_alpha()
objeto2 = pygame.image.load("objeto_2.png").convert_alpha()
objeto3 = pygame.image.load("objeto_3.png").convert_alpha()
objeto4 = pygame.image.load("objeto_4.png").convert_alpha()
objeto5 = pygame.image.load("objeto_5.png").convert_alpha()
persona = pygame.image.load("persona.png").convert_alpha()

# Fuentes
fuente = pygame.font.Font(None, 36)

# Constantes
pos_fondo = (0, 0)

# Inicializamos la posición del personaje
pos_persona = [ancho_pantalla // 2, alto_pantalla - persona.get_height()]

# Inicializamos la posición y velocidad de los objetos
objetos = [
    {"imagen": objeto1, "rect": objeto1.get_rect(topleft=(random.randint(0, ancho_pantalla - objeto1.get_width()), 0)),
     "velocidad": random.uniform(5, 10)},
    {"imagen": objeto2, "rect": objeto2.get_rect(topleft=(random.randint(0, ancho_pantalla - objeto2.get_width()), 0)),
     "velocidad": random.uniform(5, 10)},
    {"imagen": objeto3, "rect": objeto3.get_rect(topleft=(random.randint(0, ancho_pantalla - objeto3.get_width()), 0)),
     "velocidad": random.uniform(5, 10)},
    {"imagen": objeto4, "rect": objeto4.get_rect(topleft=(random.randint(0, ancho_pantalla - objeto4.get_width()), 0)),
     "velocidad": random.uniform(5, 10)},
    {"imagen": objeto5, "rect": objeto5.get_rect(topleft=(random.randint(0, ancho_pantalla - objeto5.get_width()), 0)),
     "velocidad": random.uniform(5, 10)},
]

# Inicializamos las vidas
vidas = 3

# Velocidad del personaje
velocidad_persona = 10

# Reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Contador de tiempo
tiempo_inicio = pygame.time.get_ticks()
tiempo_pausa = 0
tiempo_partida = 0

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    # Lógica del juego
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and pos_persona[0] > 0:
        pos_persona[0] -= velocidad_persona
    if keys[K_RIGHT] and pos_persona[0] < ancho_pantalla - persona.get_width():
        pos_persona[0] += velocidad_persona

    # Mover objetos hacia abajo
    for objeto in objetos:
        objeto["rect"].move_ip(0, objeto["velocidad"])

        # Verificar colisión con el personaje
        if objeto["rect"].colliderect(pygame.Rect(pos_persona, persona.get_size())):
            objetos.remove(objeto)
            vidas -= 1
            if vidas == 0:
                pantalla.blit(coras0, (0, 0))
                pygame.display.update()
                time.sleep(3)
                pygame.quit()
                sys.exit()

        # Verificar si el objeto ha llegado al fondo
        if objeto["rect"].y > alto_pantalla:
            objeto["rect"].y = 0
            objeto["rect"].x = random.randint(0, ancho_pantalla - objeto["imagen"].get_width())
            objeto["velocidad"] = random.uniform(5, 10)

    # Calcular tiempo de partida
    if vidas > 0:
        tiempo_partida = pygame.time.get_ticks() - tiempo_inicio - tiempo_pausa

    # Limpiar pantalla
    pantalla.blit(fondo, pos_fondo)

    # Dibujar objetos
    for objeto in objetos:
        pantalla.blit(objeto["imagen"], objeto["rect"])

    # Dibujar personaje
    pantalla.blit(persona, pos_persona)

    # Dibujar vidas
    if vidas == 3:
        pantalla.blit(coras3, (0, 0))
    elif vidas == 2:
        pantalla.blit(coras2, (0, 0))
    elif vidas == 1:
        pantalla.blit(coras1, (0, 0))

    # Dibujar tiempo de partida
    tiempo_texto = fuente.render(f"Tiempo: {tiempo_partida/1000:.3f} s", True, (255, 255, 255))
    pantalla.blit(tiempo_texto, (ancho_pantalla // 2 - 100, alto_pantalla - 50))

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad del juego
    reloj.tick(30)

# Actualizar el contador de tiempo cuando el juego está en pausa
tiempo_pausa += pygame.time.get_ticks() - tiempo_pausa
