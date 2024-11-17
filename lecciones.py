import tkinter as tk
import menu



def Mostrarlecciones(parent):
    frame_lecciones = tk.Frame(parent,  background= "azure2")
    menu.Abrirmenu(frame_lecciones)    
    frame_lecciones.pack(fill="both", expand=True)
   
