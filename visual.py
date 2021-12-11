from tkinter import *
from tkinter.font import BOLD 


class UI(Frame): 
    #"""Docstring.""" 
    def __init__(self, parent=None): 
        Frame.__init__(self, parent) 
        self.parent = parent 
        
        self.init_ui()


    def init_ui(self):

        
     #ETIQUETAS
        self.parent.title("Javier´s Music")
        etiqueta_nombre = Label(self.parent, text="Nombre de la cancion: ", font=("Arial", 10, BOLD))    
        etiqueta_nombre.place(x=30,y=10)
        etiqueta_nombre_respuesta = Label(self.parent, text="", font=("Arial", 8))
        etiqueta_nombre_respuesta.place(x=200,y=10)
        
        etiqueta_artista = Label(self.parent, text="Artista: ", font=("Arial", 10, BOLD))
        etiqueta_artista.place(x=30,y=40)
        etiqueta_artista_respuesta = Label(self.parent, text="", font=("Arial", 8))
        etiqueta_artista_respuesta.place(x=200,y=40)

        etiqueta_ruta = Label(self.parent, text="Ruta: ", font=("Arial", 10, BOLD))
        etiqueta_ruta.place(x=30,y=70)
        etiqueta_ruta_respuesta = Label(self.parent, text="", font=("Arial", 8))
        etiqueta_ruta_respuesta.place(x=200,y=70)

        etiqueta_genero = Label(self.parent, text="Genero: ", font=("Arial", 10, BOLD))
        etiqueta_genero.place(x=30,y=100)
        etiqueta_genero_respuesta = Label(self.parent, text="", font=("Arial", 8))
        etiqueta_genero_respuesta.place(x=200,y=100)

        etiqueta_anio = Label(self.parent, text="Año: ", font=("Arial", 10, BOLD))
        etiqueta_anio.place(x=30,y=130)
        etiqueta_anio_respuesta = Label(self.parent, text="", font=("Arial", 8))
        etiqueta_anio_respuesta.place(x=200,y=130)
    #BOTONES
        boton_buscar = Button(self.parent, text="Buscar")
        boton_buscar.place(x=30,y=500)

    
            
    
        
        
        

       



if __name__ == "__main__":
    ROOT = Tk()
    imagen_cancion = PhotoImage(file="fondo.png")
    imagen_cancion_label = Label(ROOT, image=imagen_cancion).place(x=0,y=150)
    ROOT.geometry("800x600")
    APP = UI(parent=ROOT)
    APP.mainloop()
    ROOT.destroy()