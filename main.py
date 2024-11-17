# Inicio - Este es el codigo inicial para ejecutar el proyecto
import tkinter as tk
import juegos
import lecciones
import notas
import menu

ventana = tk.Tk()
ventana.title("PIRAMIDER")
ventana.geometry("900x600+340+100")
ventana.minsize(900, 600)
ventana.maxsize(1920, 1080)
ventana.iconbitmap("piramider.ico")

#------------------ funciones ---------------

def Vidas():
    print("El usuario tiene 10 vidas")

def Chips():
    print("El usuario tiene 10 chips")

#------------------ botones------------------------


#----------------- Frames ------------------
# frame_inicio = tk.Frame(ventana, background= "blue2")
# frame_inicio.pack( fill= "both", expand= True)

# contenedor = tk.Frame(frame_inicio, background="blue2")
# contenedor.configure(width=100, height=300)
# contenedor.pack(padx= 100, pady= 200)

# btn_inicio = tk.Button(contenedor, text="inicio", command= Abrirmenu)
# btn_inicio.config (fg="white", bg="gray",font=("Arial", 12) )
# btn_inicio.pack()

frame_principal = tk.Frame(ventana, background= "azure2")
menu.Abrirmenu(frame_principal)
frame_principal.pack(fill= "both", expand= True)


ventana.mainloop()
