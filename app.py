
from automata import AnalizadorLexico
from tkinter import *
from tkinter import Button, Label,Tk,filedialog, ttk, Frame, PhotoImage
from tkinter.font import BOLD 
from automata import AnalizadorLexico






class UI(Frame): 
    #"""Docstring.""" 
    def __init__(self, parent=None): 
        Frame.__init__(self, parent) 
        self.parent = parent 
        
        self.init_ui()


    def init_ui(self):
        a = AnalizadorLexico()     
        
        #ETIQUETAS  
        self.parent.title("Javier´s Music")
        etiqueta_nombre = Label(self.parent, text="Nombre de la cancion: ", font=("Arial", 10, BOLD))    
        etiqueta_nombre.place(x=30,y=10)
     
        
        etiqueta_artista = Label(self.parent, text="Artista: ", font=("Arial", 10, BOLD))
        etiqueta_artista.place(x=30,y=40)

        etiqueta_ruta = Label(self.parent, text="Ruta: ", font=("Arial", 10, BOLD))
        etiqueta_ruta.place(x=30,y=70)


        etiqueta_genero = Label(self.parent, text="Genero: ", font=("Arial", 10, BOLD))
        etiqueta_genero.place(x=30,y=100)


        etiqueta_anio = Label(self.parent, text="Año: ", font=("Arial", 10, BOLD))
        etiqueta_anio.place(x=30,y=130)


        etiqueta_lista = Label(self.parent, text="Lista de reproduccion", font=("Arial", 10, BOLD))
        etiqueta_lista.place(x=830,y=10)




        #BOTONES
        boton_buscar = Button(self.parent, text="Buscar", command= abrir(self))
        boton_buscar.place(x=690,y=10)


      
        

def leerArchivo():
    direcion = filedialog.askopenfilename(initialdir ='/', 
											title='Escoger Tu archivo de entrada', 
										filetype=(('mt3 files', '*.mt3*'),('All files', '*.*')))
    archivo = open(direcion, 'r')
    lineas = archivo.read()    
    return lineas

def abrir(self):
    
    a = AnalizadorLexico()
    a.analizar(leerArchivo())    
    a.seleccionar()
    pop=50

    for i in a.lista:
        etiqueta_anio_respuesta = Label(self.parent, text="-"+ i[0], font=("Arial", 8))
        etiqueta_anio_respuesta.place(x=830,y=pop)
        pop = pop + 30

    etiqueta_nombre_respuesta = Label(self.parent, text= a.lista[0][0], font=("Arial", 8))
    etiqueta_nombre_respuesta.place(x=200,y=10)     

    etiqueta_artista_respuesta = Label(self.parent, text=a.lista[0][1], font=("Arial", 8))
    etiqueta_artista_respuesta.place(x=200,y=40)    

    etiqueta_ruta_respuesta = Label(self.parent, text=a.lista[0][2], font=("Arial", 8))
    etiqueta_ruta_respuesta.place(x=200,y=70)

    etiqueta_genero_respuesta = Label(self.parent, text=a.lista[0][3], font=("Arial", 8))
    etiqueta_genero_respuesta.place(x=200,y=100)

    etiqueta_anio_respuesta = Label(self.parent, text=a.lista[0][4], font=("Arial", 8))
    etiqueta_anio_respuesta.place(x=200,y=130)

if __name__ == "__main__":
    ROOT = Tk()
    imagen_cancion = PhotoImage(file="fondo.png")
    imagen_cancion_label = Label(ROOT, image=imagen_cancion).place(x=0,y=150)
    imagen1  = PhotoImage(file ='iniciar.png')
    imagen2  = PhotoImage(file ='stop.png')
    imagen3  = PhotoImage(file ='pausa.png')
    imagen4 = PhotoImage(file ='continuar.png')
    imagen5 = PhotoImage(file ='retroceder.png')
    imagen6 = PhotoImage(file ='adelantar.png')

    boton2 = Button(ROOT, image= imagen1 )
    boton2.place(x=30,y=500)


    boton3 = Button(ROOT,image= imagen2)
    boton3.place(x=100,y=500)
        
    boton4 = Button(ROOT,image= imagen3)
    boton4.place(x=170,y=500)
        
    boton5 = Button(ROOT, image= imagen4)
    boton5.place(x=240,y=500)
        
    atras = Button(ROOT, image= imagen5)
    atras.place(x=310,y=500)
       
    adelante = Button(ROOT, image= imagen6)
    adelante.place(x=380,y=500)
    ROOT.geometry("1000x600")
    APP = UI(parent=ROOT)
    APP.mainloop()
    ROOT.destroy()
