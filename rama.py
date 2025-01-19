from archivo import Archivo
from commit import Commit
class Rama:
    def __init__(self, nombre:str, ultimo_commit:Commit = None):
        self.nombre = nombre
        self.ultimo_commit = ultimo_commit
    
    def nuevo_commit(self, ultimo_commit:Commit):
        self.ultimo_commit = ultimo_commit

lista = [Archivo("texto1.txt","1234567890"),Archivo("texto2.txt","qwertyuiop"),Archivo("texto3.txt","asdfghjkl"),Archivo("texto4.txt","zxcvbnm,"),Archivo("texto4.txt","zsefcbhjuik,")]
c1 = Commit("Primer Commit",lista,None)
r1 = Rama("Master")
r1.nuevo_commit(c1)
lista = [Archivo("texto5.txt","1234567890"),Archivo("texto2.txt","qwertyuiop"),Archivo("texto3.txt","asdfghjkl"),Archivo("texto4.txt","zxcvbnm,"),Archivo("texto4.txt","zsefcbhjuik,")]
c2 = Commit("Segundo Commit", lista, c1)
r1.nuevo_commit(c2)

