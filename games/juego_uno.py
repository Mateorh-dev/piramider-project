#import tkinter as tk
import pygame
import random as r
import constantes_globales as cg
from objetos_juego_uno import *
'''
# Codigo Tkinter

ventana = tk.Tk()
#ventana.title("PIRAMIDER")
#Tamaño (ancho x alto)
ventana.geometry(f"{cg.ancho_ventana}x{cg.alto_ventana}")
ventana.minsize(cg.ancho_ventana, cg.alto_ventana)

cont_descripcion = tk.Frame(ventana)
cont_descripcion.configure(width = cg.ancho_descripcion,height = cg.alto_descripcion)

zona_juego = tk.Frame(ventana)
zona_juego.configure(width = cg.ancho_juego,height = cg.alto_juego)

cont_descripcion.pack()
zona_juego.pack()
ventana.mainloop()
'''
# Codigo Pygame

pc = Computador()
plancha = PlCorte()

bateria_pc = s.bateria
dduro_pc = s.dduro
ram_pc = s.ram
ventilador_pc = s.ventilador

componenetes_pc = [bateria_pc, dduro_pc, ram_pc, ventilador_pc]
r.shuffle(componenetes_pc)
lobj_componenetes_pc = []

#Creacion de Objetos
for c in componenetes_pc:
    nuevo_comp = ElementoInteractivo(c)
    lobj_componenetes_pc.append(nuevo_comp)

#Espacio y posicion entre objetos
suma_ancho = 0
for n in lobj_componenetes_pc:
    suma_ancho += n.get_ancho()

num_componenetes_pc = len(lobj_componenetes_pc)
espacio_componenetes = (cg.ancho_juego - suma_ancho)/(num_componenetes_pc + 1)

espacio = 0
for e in lobj_componenetes_pc:
    espacio += espacio_componenetes
    e.set_px(espacio)
    espacio += e.get_ancho()

pygame.init()

game_screen = pygame.display.set_mode((cg.ancho_juego,cg.alto_juego))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    click = pygame.mouse.get_pressed()[0]
    posicion = pygame.mouse.get_pos()
    movimiento = pygame.mouse.get_rel()

    plancha.dibujar(game_screen)
    pc.dibujar(game_screen)
       
    for d in lobj_componenetes_pc:
        d.set_posicion(click,posicion,movimiento)
        d.dibujar(game_screen)

    pygame.display.update()

pygame.quit()