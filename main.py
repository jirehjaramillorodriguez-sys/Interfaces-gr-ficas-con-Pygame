#aqui colocaré casi que lo mismo pero aplicando las clases de poo
import pygame
#estaa es la clase del botón, nos permite diseñarlo y decir si pulsamos el mouse dentro del botón
class Boton:
    def __init__(self, x, y, ancho, alto, texto):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto

    def dibujar(self, screen, fuente):
        pygame.draw.rect(screen, "red", self.rect)
        texto = fuente.render(self.texto, True, "white")
        screen.blit(texto, (self.rect.x + 50, self.rect.y + 30))

    def fue_clickeado(self, pos_mouse):
        return self.rect.collidepoint(pos_mouse)
#esta es la clase que hace la mayoría de cosas, crea la ventana, crea el botón, tiene el contador para que aumente cuando se pulsa el botón
class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.fuente = pygame.font.Font(None, 50)
        self.contador = 0
#Aqui le decimos al botón dónde va y qué tan grande es
#basicamente lo que hacemos con el self es decirle a la clase que lo guarde
        self.boton = Boton(300, 250, 200, 100, "SUMAR")
        self.running = True
    def manejar_evento(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.boton.fue_clickeado(event.pos):
                self.contador = self.contador + 1
    def dibujar_todo(self):
        self.screen.fill("purple")
        self.boton.dibujar(self.screen, self.fuente)
        texto = self.fuente.render(f"Contador: {self.contador}", True, "white")
        self.screen.blit(texto, (300, 100))
        pygame.display.flip()
    def correr(self):
        while self.running:
            for event in pygame.event.get():
                self.manejar_evento(event)
            self.dibujar_todo()
        pygame.quit()

mi_app = App()
mi_app.correr()