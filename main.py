# Inicio - Este es el codigo inicial para ejecutar el proyecto
import tkinter as tk

ventana = tk.Tk()
ventana.title("PIRAMIDER")
ventana.geometry("900x600+340+100")
ventana.minsize(900, 600)
ventana.maxsize(1920, 1080)
ventana.configure (bg="azure")
ventana.iconbitmap("piramider-project/piramider.ico")


#----------------- Frames ------------------

menu = tk.Frame(ventana)
menu.configure(width=1080, height=20, bg= "Blue" )
menu.pack(fill="x")

contenedor = tk.Frame(menu)
contenedor.configure(width=1040, height=20, bg= "Blue" )
contenedor.pack()

anuncios=tk.Frame(ventana)
anuncios.configure( width=600, height=200,bg= "blue")
anuncios.pack(padx=100,pady=50)


boton= tk.Button(menu, text="Principal")
boton.config(fg= "white", bg= "blue", font=("Arial", 12))
boton.pack(side="left", padx=5,)

#------------------ funciones ---------------

def Abrirjuegos():     
    print("abrio los juegos")

def Abrirnotas():
    print("abrio las notas")

def Abrirlecciones():
    print("abrio las lecciones")

def Vidas():
    print("El usuario tiene 10 vidas")
def Chips():
    print("El usuario tiene 10 chips")

#------------------ botones------------------------

boton1= tk.Button(menu, text="Lecciones", command = Abrirlecciones)
boton1.config(fg= "white", bg= "blue", font=("Arial", 12))
boton1.pack(side="left", padx=5)

boton2=tk.Button(menu, text="Notas", command = Abrirnotas)
boton2.config(fg= "white", bg= "blue", font=("Arial", 12))
boton2.pack(side="left", padx=5)

boton3= tk.Button(menu, text="Juegos", command = Abrirjuegos)
boton3.config(fg= "white", bg= "blue", font=("Arial", 12)) 
boton3.pack(side="left", padx=5)

chips_boton= tk.Button(menu, text="Chips", command = Chips )
chips_boton.config(fg="white", bg="red",font=("Arial", 12) )
chips_boton.pack(side="right", padx= 5)

vidas_boton= tk.Button(menu, text="Vidas", command = Vidas )
vidas_boton.config(fg="white", bg="red",font=("Arial", 12) )
vidas_boton.pack(side="right", padx= 5)




ventana.mainloop()
