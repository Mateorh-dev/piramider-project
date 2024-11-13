import pygame
import constantes_globales as cg
import sprites as s

def CalcularForma(sprite,px,py):
    return pygame.Rect(px,py,sprite.get_width(),sprite.get_height())

class Componente:
    def __init__(self, img):
        self.__image = img
        self.__rect = self.__image.get_rect()
        #Posicion inicial por defecto
        self.forma = CalcularForma(self.__image,0,0)
    def dibujar(self, ventana):
        ventana.blit(self.__image, self.forma)
    def get_image(self):
        return self.__image
    def get_ancho(self):
        return self.__rect.size[0]

class PlCorte(Componente):
    def __init__(self):
        super().__init__(s.plcorte)

class Computador(Componente):
    def __init__(self):
        super().__init__(s.computador)
        self.forma.x = ((cg.ancho_juego-cg.computador_ancho)/2)

class ElementoInteractivo(Componente):
    def __init__(self, img):
        super().__init__(img)
        self.forma.y = 480
        self.mover = False
        
    def set_px(self,px):
        self.forma.x = px
    def set_posicion(self, click,posicion,movimiento):
        
        #posicion = pygame.mouse.get_pos()
        #movimiento = pygame.mouse.get_rel()
        
        if self.forma.collidepoint(posicion):
            if click:
                self.mover = True
                
            else:
                self.mover = False
        if self.mover:
        #    self.forma.move_ip(movimiento)
            self.forma.x += movimiento[0]
            self.forma.y += movimiento[1]