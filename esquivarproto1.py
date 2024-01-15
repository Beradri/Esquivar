import pygame
from pygame.locals import *
import sys
import time

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

# Constantes
pos_fondo = (0, 0)



