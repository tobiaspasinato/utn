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
reiniciar = font.render("Reiniciar", True, (0, 0, 0))
pregunta = font.render("Pregunta", True, (0, 0, 0))
text_score = font.render("Score:", True, (0, 0, 0))

score = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            event.pos
        if (event.pos[0] > 320 and event.pos[0] < 500) and (event.pos[1] < 500 and event.pos[1] > 450):
            print("text")
    
    screen.fill(COLOR_GOJO)# Se pinta el fondo de la ventana
    screen.blit(imagen_gojo,(50,50))
    pygame.draw.rect(screen, COLOR_GOJO2, (250, 50, 230, 50))
    pygame.draw.rect(screen, COLOR_GOJO2, (250, 115, 230, 50))
    pygame.draw.rect(screen, COLOR_GOJO2, (0, 450, 180, 50))
    pygame.draw.rect(screen, COLOR_GOJO2, (320, 450, 180, 50))
    screen.blit(text,(260,60))
    screen.blit(reiniciar,(10,460))
    screen.blit(pregunta,(335,460))
    screen.blit(text_score,(260,125))
    pygame.display.flip()# Muestra los cambios en la pantalla

pygame.quit() # Fin