from    tkinter import *
ventana = Tk()
ventana.config(bg="black")
ventana.title("Pruebas")
ventana.geometry("400x400")

#agregar imagen
imagen = PhotoImage(file="fondo.png")
lblImagen = Label(ventana, image=imagen).place(x=0, y=0)
ventana.mainloop()