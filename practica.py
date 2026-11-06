# Eemplo
import pygame


pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
contador = 0
boton = pygame.Rect(300, 250, 200, 100)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if boton.collidepoint(event.pos):
                contador = contador + 1

    screen.fill("purple")

    boton = pygame.Rect(300, 250, 200, 100)
    pygame.draw.rect(screen, "red", boton)

    fuente = pygame.font.Font(None, 50)
    texto_contador = fuente.render(f"Contador: {contador}", True, "white")
    screen.blit(texto_contador, (300, 100))

    texto_boton = fuente.render("SUMAR", True, "white")
    screen.blit(texto_boton, (340, 280))

    pygame.display.flip()

pygame.quit()