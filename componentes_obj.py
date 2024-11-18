# En este espacio se crearan los objetos que se usaran en la interfaz
import tkinter as tk

class ObjBoton(tk.Button):
    def __init__(self,espacio,texto,funcion):
        super().__init__(espacio, text=f"{texto}",command=funcion)
        self.config(fg= "white", font=("Arial", 12))
        self.pack(padx=4)
    def set_config_color(self, color):
        self.config(bg=color)

    def set_pack_align(self, orientacion):
        self.pack(side=orientacion)        

class BotonAzul(ObjBoton):
    def __init__(self,espacio,texto,funcion):
        super().__init__(espacio,texto,funcion)
        self.set_config_color("blue")
        self.set_pack_align("left")

class BotonRojo(ObjBoton):
    def __init__(self,espacio,texto,funcion):
        super().__init__(espacio,texto,funcion)
        self.set_config_color("red")
        self.set_pack_align("right")

class BotonGris(ObjBoton):
    def __init__(self,espacio,texto,funcion):
        super().__init__(espacio,texto,funcion)
        self.set_config_color("grey")
        self.set_pack_align("right")

class AbrirVentana:
    def __init__(self,titulo, mensaje, tamaño, ventana):
        self.nueva_ventana = tk.Toplevel(ventana)
        self.nueva_ventana.title(titulo)
        self.nueva_ventana.iconbitmap("icon/piramider.ico")
        self.nueva_ventana.geometry(tamaño)
        self.nueva_ventana.configure(bg="snow")

        self.etiqueta = tk.Label(self.nueva_ventana, text=mensaje, font=("Arial", 20), fg="blue", bg="snow")
        self.etiqueta.pack(pady=50)

        self.frame_anuncios = tk.Frame(self.nueva_ventana, bg="lightgray", width=700, height=300)
        self.frame_anuncios.pack(pady=30, expand=True)

        self.boton_cerrar = tk.Button(self.nueva_ventana, text="volver", command=self.nueva_ventana.destroy, font=("Arial", 12), bg="red", fg="white")
        self.boton_cerrar.place(x=0, y=0)
        self.boton_cerrar.pack()