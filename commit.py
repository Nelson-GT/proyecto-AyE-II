import random
from archivo import Archivo
class Commit:
    
    def __init__(self, comentario: str, archivos: Archivo, anterior:'Commit'):      #Constructor de la clase
        self.cometario = comentario
        self.archivos = archivos
        self.anterior = anterior
        self.hash = self.crear_Hash()
    
    
    def crear_Hash(self):                           #función para crear el hash aleatorio del commit
        letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        hash = ""
        for k in range(12):             #añade a hash un elemento aleatorio de la lista para crear un hash de 12 caracteres
            hash += letras[random.randint(0,len(letras)-1)]
        return hash