from automata import AnalizadorLexico


def leerArchivo(ruta):
    archivo = open(ruta, "r")
    lineas = archivo.read()    
    return lineas

if __name__ == "__main__":
    a = AnalizadorLexico()   
    a.analizar(leerArchivo("pruebas.txt"))     
    a.seleccionar()