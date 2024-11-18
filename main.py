# Inicio - Este es el codigo inicial para ejecutar el proyecto
import tkinter as tk

ventana = tk.Tk()
ventana.title("PIRAMIDER")
ventana.geometry("900x600+340+100")
ventana.minsize(900, 600)
ventana.maxsize(1920, 1080)
ventana.iconbitmap("piramider.ico")

#---------------------------------------------------------------

def abrir_ventana(titulo, mensaje, tamaño):
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title(titulo)
    nueva_ventana.iconbitmap("piramider.ico")
    nueva_ventana.geometry(tamaño)
    nueva_ventana.configure(bg="snow")


    etiqueta = tk.Label(nueva_ventana, text=mensaje, font=("Arial", 20), fg="blue", bg= "snow")
    etiqueta.pack(pady=50)
 
    frame_anuncios = tk.Frame(nueva_ventana, bg="lightgray", width=700, height= 300)
    frame_anuncios.pack(pady= 30, expand= True)

    boton_cerrar = tk.Button(nueva_ventana, text="volver", command=nueva_ventana.destroy, font=("Arial", 12), bg="red", fg="white")
    boton_cerrar.place(x=0, y=0)
    boton_cerrar.pack()


#-------------------------------------------------


def abrir_juegos():
    abrir_ventana("Juegos",  "Juegos", "900x600+340+100")

def abrir_lecciones():
    abrir_ventana("Lecciones", "Lecciones.", "900x600+340+100")

def abrir_apuntes():
    abrir_ventana("Apuntes", "Apuntes.", "900x600+340+100")

def abrir_vidas():
    abrir_ventana("vidas", "El usuario tiene 10 vidas", "100x300")
    
def abrir_Chips():
    abrir_ventana("chips", "El usuario tiene 10 chips", "100x300")

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
boton_juegos = tk.Button(conten_menu, text="Juegos", command=abrir_juegos)
boton_juegos.config(fg="white", bg="blue2", font=("Arial", 12))
boton_juegos.pack(side="left", padx = 4)

boton_lecciones = tk.Button(conten_menu, text="Lecciones", command=abrir_lecciones)
boton_lecciones.config(fg="white", bg="blue2", font=("Arial", 12))
boton_lecciones.pack(side="left", padx = 4)

boton_apuntes = tk.Button(conten_menu, text="Apuntes", command=abrir_apuntes)
boton_apuntes.config(fg="white", bg="blue2", font=("Arial", 12))
boton_apuntes.pack(side="left", padx =4)

boton_vidas = tk.Button(conten_menu,text="Vidas", command= abrir_vidas )
boton_vidas.config(fg= "white",bg="red", font=("Arial", 12) )
boton_vidas.pack(side="right",padx = 4 )

boton_chips = tk.Button(conten_menu,text="Chips", command= abrir_Chips )
boton_chips.config(fg= "white",bg="gray", font=("Arial", 12) )
boton_chips.pack(side="right",padx = 4 )


ventana.mainloop()

