import pygame
from constantes import *
from datos import *

lista_preguntas = []
lista_a = []
lista_b = []
lista_c = []
lista_correcta = []

for pregunta in lista:
    lista_preguntas.append(pregunta["pregunta"])
    lista_a.append(pregunta["a"])
    lista_b.append(pregunta["b"])
    lista_c.append(pregunta["c"])
    lista_correcta.append(pregunta["correcta"])

score = 0
vidas = 0
game_over = False
bandera_habilitar_opciones = False
boton_a = False
boton_b = False
boton_c = False
botones = False
posi_preg = -1
running = True

pygame.init() #Se inicializa pygame

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Preguntados Gojo")
imagen_gojo = pygame.image.load("preguntados\gojo2.jpg")
imagen_gojo = pygame.transform.scale(imagen_gojo, (150, 150))
font = pygame.font.SysFont("Arial Narrow", 50)
font2 = pygame.font.SysFont("Arial Narrow", 24)
font3 = pygame.font.SysFont("Arial Narrow", 70)
text = font.render("Preguntados", True, (0, 0, 0))
reiniciar = font.render("Reiniciar", True, (0, 0, 0))
pregunta = font.render("Pregunta", True, (0, 0, 0))
text_score = font.render(f"Score: {score}", True, (0, 0, 0))
text_a = font.render("A", True, (0, 0, 0))
text_b = font.render("B", True, (0, 0, 0))
text_c = font.render("C", True, (0, 0, 0))
game_over_text = font3.render("GAME OVER", True, (0, 0, 0))
pregunta_texto = font2.render(f"{lista_preguntas[posi_preg]}", True, (0, 0, 0))
respuesta_texto_a = font2.render(f"A : {lista_a[posi_preg]}", True, (0, 0, 0))
respuesta_texto_b = font2.render(f"B : {lista_b[posi_preg]}", True, (0, 0, 0))
respuesta_texto_c = font2.render(f"C : {lista_c[posi_preg]}", True, (0, 0, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            mouse = event.pos
            if (mouse[0] > 320 and mouse[0] < 500) and (mouse[1] < 500 and mouse[1] > 450): #pregunta
                bandera_habilitar_opciones = True
                botones = True
                boton_a = True
                boton_b = True
                boton_c = True
                vidas = 0
                if posi_preg < len(lista_preguntas) - 1:
                    posi_preg = posi_preg + 1
                    
                else:
                    posi_preg = 16
            if botones == True:
                if (mouse[0] > 0 and mouse[0] < 180) and (mouse[1] < 500 and mouse[1] > 450): #reiniciar
                    posi_preg = 0
                    score = 0
                if (mouse[0] > 35 and mouse[0] < 130) and (mouse[1] < 390 and mouse[1] > 340): #a
                    if lista_correcta[posi_preg] == "a" and boton_a == True and botones == True:
                        if vidas < 2:
                            score = score + 10
                        boton_a = False
                        botones = False
                    elif lista_correcta[posi_preg] != "a" and boton_a == True and botones == True:
                        boton_a = False
                        botones = True
                        vidas = vidas + 1
                if (mouse[0] > 200 and mouse[0] < 300) and (mouse[1] < 390 and mouse[1] > 340): #B
                    if lista_correcta[posi_preg] == "b" and boton_b == True and botones == True:
                        if vidas < 2:
                            score = score + 10
                        boton_b = False
                        botones = False
                    elif lista_correcta[posi_preg] != "B" and boton_b == True and botones == True:
                        boton_b = False
                        botones = True
                        vidas = vidas + 1
                if (mouse[0] > 360 and mouse[0] < 460) and (mouse[1] < 390 and mouse[1] > 340): #c
                    if lista_correcta[posi_preg] == "c" and boton_c == True and botones == True:
                        if vidas < 2:
                            score = score + 10
                        boton_c = False
                        botones = False
                    elif lista_correcta[posi_preg] != "c" and boton_c == True and botones == True:
                        boton_c = False
                        botones = True
                        vidas = vidas + 1
    
    text_score = font.render(f"Score: {score}", True, (0, 0, 0))
    text_a = font.render("A", True, (0, 0, 0))
    text_b = font.render("B", True, (0, 0, 0))
    text_c = font.render("C", True, (0, 0, 0))
    pregunta_texto = font2.render(f"{lista_preguntas[posi_preg]}", True, (0, 0, 0))
    respuesta_texto_a = font2.render(f"A : {lista_a[posi_preg]}", True, (0, 0, 0))
    respuesta_texto_b = font2.render(f"B : {lista_b[posi_preg]}", True, (0, 0, 0))
    respuesta_texto_c = font2.render(f"C : {lista_c[posi_preg]}", True, (0, 0, 0))
    screen.fill(COLOR_GOJO)# Se pinta el fondo de la ventana
    screen.blit(imagen_gojo,(50,50))
    pygame.draw.rect(screen, COLOR_GOJO2, (250, 50, 230, 50)) #titulo
    pygame.draw.rect(screen, COLOR_GOJO2, (250, 115, 230, 50)) #score
    pygame.draw.rect(screen, COLOR_GOJO2, (0, 450, 180, 50)) # reiniciar
    pygame.draw.rect(screen, COLOR_GOJO2, (320, 450, 180, 50)) #pregunta next
    # pygame.draw.rect(screen, COLOR_GOJO2, (10, 220, 480, 110)) #pregunta
    if bandera_habilitar_opciones == True:
        pygame.draw.rect(screen, COLOR_GOJO2, (10, 220, 480, 110)) #pregunta
        screen.blit(pregunta_texto,(20,230))
        screen.blit(respuesta_texto_a,(20,260))
        screen.blit(respuesta_texto_b,(20,285))
        screen.blit(respuesta_texto_c,(20,310))
        if boton_a == True:
            pygame.draw.rect(screen, COLOR_GOJO2, (30, 340, 100, 50)) #a
            screen.blit(text_a,(65,350))
        if boton_b == True:
            pygame.draw.rect(screen, COLOR_GOJO2, (200, 340, 100, 50)) #B
            screen.blit(text_b,(235,350))
        if boton_c == True:
            pygame.draw.rect(screen, COLOR_GOJO2, (360, 340, 100, 50)) #C
            screen.blit(text_c,(390,350))
    screen.blit(text,(260,60))
    screen.blit(reiniciar,(10,460))
    screen.blit(pregunta,(335,460))
    screen.blit(text_score,(260,125))
    pygame.display.flip()# Muestra los cambios en la pantalla
pygame.quit() # Fin