import pygame
from constantes import *
from functions import *

pygame.init() #Se inicializa pygame

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Preguntados Gojo")
imagen_gojo = pygame.image.load("preguntados\gojo2.jpg")
imagen_gojo = pygame.transform.scale(imagen_gojo, (150, 150))
font = pygame.font.SysFont("Arial Narrow", 50)
text = font.render("Preguntados", True, (0, 0, 0))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            print(event.pos)
    
    screen.fill(COLOR_GOJO)# Se pinta el fondo de la ventana
    screen.blit(imagen_gojo,(50,50))
    pygame.draw.rect(screen, COLOR_GOJO2, (250, 50, 230, 50))
    screen.blit(text,(260,60))
    pygame.display.flip()# Muestra los cambios en la pantalla

pygame.quit() # Fin