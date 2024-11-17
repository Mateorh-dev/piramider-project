import tkinter as tk
import menu

def Mostrarjuegos(parent):
    frame_juegos = tk.Frame(parent, background= "azure2")
    menu.Abrirmenu(frame_juegos) 
    frame_juegos.pack(fill="both", expand=True)


