import pygame
import games.constantes_globales as cg

plcorte = pygame.transform.scale(pygame.image.load("games/picture/plcorte.png"),
                               (cg.ancho_juego,cg.alto_juego))

computador = pygame.transform.scale(pygame.image.load("games/picture/computador.png"),
                               (cg.computador_ancho,cg.computador_alto))

bateria = pygame.transform.scale(pygame.image.load("games/picture/bateria.png"),
                               (cg.bateria_ancho,cg.bateria_alto))

dduro = pygame.transform.scale(pygame.image.load("games/picture/dduro.png"),
                               (cg.dduro_ancho,cg.dduro_alto))

ram = pygame.transform.scale(pygame.image.load("games/picture/ram.png"),
                               (cg.ram_ancho,cg.ram_alto))

ventilador = pygame.transform.scale(pygame.image.load("games/picture/ventilador.png"),
                               (cg.ventilador_ancho,cg.ventilador_alto))