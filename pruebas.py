from tkinter import Button, Label,Tk,filedialog, ttk, Frame, PhotoImage

def leerArchivo():
    direcion = filedialog.askopenfilename(initialdir ='/', 
											title='Escoger Tu archivo de entrada', 
										filetype=(('mt3 files', '*.mt3*'),('All files', '*.*')))
    archivo = open(direcion, 'r')
    print(archivo.read())
    archivo.close()

#iniciar
root = Tk()
Button(root, text="Buscar", command=leerArchivo).pack()
root.mainloop()
