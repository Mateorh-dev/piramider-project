# Inicio - Este es el codigo inicial para ejecutar el proyecto
import tkinter as tk
from componentes_obj import *
from games import juego_uno as juno

ventana = tk.Tk()
ventana.title("PIRAMIDER")
ventana.geometry("900x600+340+100")
ventana.minsize(900, 600)
ventana.maxsize(1920, 1080)
ventana.iconbitmap("icon/piramider.ico")

#-------------------------------------------------

def abrir_juegos():
    juno.StartArmandoMiPc()
    #AbrirVentana("Juegos",  "Juegos", "900x600+340+100", ventana)

def abrir_lecciones():
    AbrirVentana("Lecciones", "Lecciones.", "900x600+340+100", ventana)

def abrir_apuntes():
    AbrirVentana("Apuntes", "Apuntes.", "900x600+340+100", ventana)

def abrir_vidas():
    AbrirVentana("vidas", "El usuario tiene 10 vidas", "500x300+550+250", ventana)
    
def abrir_Chips():
    AbrirVentana("chips", "El usuario tiene 10 chips", "500x300+550+250", ventana)

# ----------------------------- Frames ------------------------

frame_principal=tk.Frame(ventana, bg="snow")
frame_principal.pack(fill="both", expand= True)

menu = tk.Frame(frame_principal, bg="blue2", height=70)
menu.pack(fill="both")

conten_menu =  tk.Frame(menu, bg="blue2")
conten_menu.pack( fill="x", pady=0)


frame_anuncios = tk.Frame(frame_principal, bg="lightgray", width=700, height= 300)
frame_anuncios.pack(pady= 30)

#------------------ botones------------------------

btn_juegos = BotonAzul(menu,"Juegos", abrir_juegos)
btn_lecciones = BotonAzul(menu,"Lecciones", abrir_lecciones)
btn_apuntes = BotonAzul(menu,"Apuntes", abrir_apuntes)
btn_vidas = BotonRojo(menu,"Vidas", abrir_vidas)
btn_chips = BotonGris(menu,"Chips", abrir_Chips)

ventana.mainloop()