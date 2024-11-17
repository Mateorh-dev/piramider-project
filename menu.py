import tkinter as tk
import juegos
import lecciones
import notas

ventana = tk.Tk()
ventana.title("PIRAMIDER")
ventana.geometry("900x600+340+100")
ventana.minsize(900, 600)
ventana.maxsize(1920, 1080)
ventana.iconbitmap("piramider.ico")

def Abrirjuegos():
    juegos.Mostrarjuegos(ventana)

def Abrirlecciones():
    juegos.Mostrarleciones(ventana)

def Abrirnotas():
    juegos.Mostrarnotas(ventana)

def Abrirmenu(parent):
    menu = tk.Frame(parent)
    menu.configure(width=1080, height=20, bg= "blue2" )
    contenedor = tk.Frame(menu)
    contenedor.configure(width=1040, height=20, bg= "blue2" )
    menu.pack(fill= "x")
    contenedor.pack()

    # boton= tk.Button(menu, text="Principal", command= contenedor.destroy)
    # boton.config(fg= "white", bg= "blue2", font=("Arial", 12))
    # boton.pack(side="left", padx=5,)

    boton1= tk.Button(menu, text="Lecciones", command = Abrirlecciones)
    boton1.config(fg= "white", bg= "blue2", font=("Arial", 12))
    boton1.pack(side="left", padx=5)

    boton2=tk.Button(menu, text="Notas", command = Abrirnotas)
    boton2.config(fg= "white", bg= "blue2", font=("Arial", 12))
    boton2.pack(side="left", padx=5)

    boton3= tk.Button(menu, text="Juegos", command = Abrirjuegos)
    boton3.config(fg= "white", bg= "blue2", font=("Arial", 12)) 
    boton3.pack(side="left", padx=5)

