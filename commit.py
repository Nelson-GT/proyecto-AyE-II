import random
from archivo import Archivo
class Commit:
    
    def __init__(self, comentario: str, archivos: Archivo, anterior:'Commit'):
        self.cometario = comentario
        self.archivos = archivos
        self.anterior = anterior
        self.hash = self.crear_Hash()
    
    @staticmethod
    def crear_Hash():
        letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        hash = ""
        for k in range(12):
            hash += letras[random.randint(0,len(letras)-1)]
        return hash

lista = [Archivo("texto1.txt","1234567890"),Archivo("texto2.txt","qwertyuiop"),Archivo("texto3.txt","asdfghjkl"),Archivo("texto4.txt","zxcvbnm,"),Archivo("texto4.txt","zsefcbhjuik,")]
c1 = Commit("Primer Commit",lista,None)
