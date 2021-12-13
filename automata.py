from Token import Token
from Token import Token_Error

class AnalizadorLexico:
    def __init__(self):
        self.listtoken = []
        self.listError = []

    def analizar(self, archivo):
        self.listtoken = []
        self.listError = []
        
        archivo += '@'
        linea = 1
        columna = 1
        indice = 0
        buffer = ""
        estado = 'A'

        while indice < len(archivo):
            caracter = archivo[indice]
            
            if estado == 'A':

                #Caracteres especiales
                if caracter == '=':
                    buffer += caracter
                    columna += 1
                    estado = 'A'
                    self.listtoken.append(Token(buffer,'IGUAL', linea, columna))
                    buffer = ""
                elif caracter == '>':
                    buffer += caracter
                    columna += 1
                    estado = 'A'
                    self.listtoken.append(Token(buffer,'MAYOR', linea, columna))
                    buffer = ""   
                elif caracter == ';':
                    buffer += caracter
                    columna += 1
                    estado = 'A'
                    self.listtoken.append(Token(buffer,'PUNTOYCOMA', linea, columna))
                    buffer = ""
                elif caracter == ':':
                    buffer += caracter
                    columna += 1
                    estado = 'A'
                    self.listtoken.append(Token(buffer,'DOSPUNTOS', linea, columna))
                    buffer = ""
                elif caracter == ',':
                    buffer += caracter
                    columna += 1
                    estado = 'A'
                    self.listtoken.append(Token(buffer,'COMA', linea, columna))
                    buffer = ""
                elif caracter == '{':
                    buffer += caracter
                    columna += 1
                    estado = 'A'
                    self.listtoken.append(Token(buffer,'LLAVEIZQ', linea, columna))
                    buffer = ""
                elif caracter == '}':
                    buffer += caracter
                    columna += 1
                    estado = 'A'
                    self.listtoken.append(Token(buffer,'LLAVEDER', linea, columna))
                    buffer = ""
                elif caracter == '[':
                    buffer += caracter
                    columna += 1
                    estado = 'A'
                    self.listtoken.append(Token(buffer,'CORCHETEIZQ', linea, columna))
                    buffer = ""
                elif caracter == ']':
                    buffer += caracter
                    columna += 1
                    estado = 'A'
                    self.listtoken.append(Token(buffer,'CORCHETEDER', linea, columna))
                    buffer = ""
                elif caracter == '(':
                    buffer += caracter
                    columna += 1
                    estado = 'A'
                    self.listtoken.append(Token(buffer,'PARENTESISIZQ', linea, columna))
                    buffer = ""
                elif caracter == ')':
                    buffer += caracter
                    columna += 1
                    estado = 'A'
                    self.listtoken.append(Token(buffer,'PARENTESISDER', linea, columna))
                    buffer = ""
                elif caracter == '"':
                   
                    columna += 1
                    estado = 'C'
                elif caracter == "'":
                    
                    columna += 1
                    estado = 'D'

                #Palabras reservadas
                elif caracter.isalpha() and not caracter.isdigit():
                    buffer += caracter
                    columna += 1
                    estado = 'B'

                elif caracter.isdigit():
                    buffer += caracter
                    columna += 1
                    estado = 'E'

               #Espacios y enter
                elif caracter == '\n':
                        linea += 1
                        columna = 1
                        estado = 'A'
                elif caracter == ' ':
                        columna += 1
                        estado = 'A'
                elif caracter == '\t':
                        columna += 1
                        estado = 'A'

                #Caracter de finalización
                elif caracter == '@':
                    indice += 100
                else:
                    self.listError.append(Token_Error('Error lexico', caracter, linea, columna))
                    indice += 1
                    
                
            #Analisis de palabras reservadas
            elif estado == 'B':
                if caracter.isalpha() and not caracter.isnumeric():
                    buffer += caracter
                    columna += 1
                    estado = 'B'
                else:
                    if buffer == 'REPLIST' or buffer == 'replist':                        
                        
                        self.listtoken.append(Token(buffer,'REPLIST', linea, columna))
                        estado = 'A'
                        buffer = ""                        

                    elif buffer == 'NOMBRE' or buffer == 'nombre':                        
                        
                        self.listtoken.append(Token(buffer,'NOMBRE', linea, columna))
                        estado = 'A'
                        buffer = ""
                        

                    elif buffer == 'ARTISTA' or buffer == 'artista':                        
                        
                        self.listtoken.append(Token(buffer,'ARTISTA', linea, columna))
                        
                        estado = 'A'
                        buffer = ""

                    elif buffer == 'RUTA' or buffer == 'ruta':                        
                        
                        self.listtoken.append(Token(buffer,'RUTA', linea, columna))
                        
                        estado = 'A'
                        buffer = ""

                    elif buffer == 'GENERO' or buffer == 'genero':                        
                        
                        self.listtoken.append(Token(buffer,'GENERO', linea, columna))
                        
                        estado = 'A'
                        buffer = ""

                    elif buffer == 'ANIO' or buffer == 'anio':                        
                        
                        self.listtoken.append(Token(buffer,'ANIO', linea, columna))
                        
                        estado = 'A'
                        buffer = ""

                    elif buffer == 'REPETIR' or buffer == 'repetir':                        
                        
                        self.listtoken.append(Token(buffer,'REPETIR', linea, columna))
                        
                        estado = 'A'
                        buffer = ""
                    else:                        
                        self.listError.append(Token_Error(buffer + " No en lista de palabras reservadas",'ERROR TIPO LEXICO', linea, columna))                        
                        buffer = ""
                        estado = 'A'
                        indice += 1
                        
                    indice -= 1

            #Analisis de cadenas ""    
            elif estado == 'C':
                 if caracter == '"':
                                        
                    columna += 1
                    estado = 'A'
                    self.listtoken.append(Token(buffer,'CADENA', linea, columna))
                    buffer = ""

                 elif caracter != "'" and caracter != ',' and caracter != '\n':
                    buffer += caracter
                    columna += 1
                    estado = 'C'

                 else:
                    self.listError.append(Token_Error('Error Sintáctico, no se cerro la cadena de texto', caracter, linea, columna))
                    buffer = ""
                    estado = 'A'
                    indice += 1

            #Analisis de cadenas ''
            elif estado == 'D':
                if caracter == "'":                    
                    columna += 1
                    estado = 'A'
                    self.listtoken.append(Token(buffer,'CADENA', linea, columna))
                    buffer = ""
                

                elif caracter != "'" and caracter != ',' and caracter != '}' and caracter != '\n':                   
                    buffer += caracter
                    columna += 1
                    estado = 'D'
                else:
                    self.listError.append(Token_Error('Error Sintáctico, no se cerro la cadena de texto', caracter, linea, columna))
                    buffer = ""
                    estado = 'A'
                    indice += 1
                
            #Analisis de numeros
            elif estado == 'E':
                if caracter.isdigit():
                    buffer += caracter
                    columna += 1
                    estado = 'E'
                else:
                    self.listtoken.append(Token(buffer,'NUMERO', linea, columna))
                    buffer = ""
                    estado = 'A'
                    indice -= 1
                


            indice += 1
    def imprimir(self):
        print("Tokens:")
        for x in self.listtoken:
            print(x.tipo, x.lexema, x.fila, x.columna)
        print("Errores:")
        for x in self.listError:
             print(x.descripcion, x.tipo, x.fila, x.columna)