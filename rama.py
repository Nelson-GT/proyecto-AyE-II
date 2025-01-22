from archivo import Archivo
from commit import Commit
class Rama:
    def __init__(self, nombre:str, ultimo_commit:Commit = None):#Constructor de la clase
        self.nombre = nombre
        self.ultimo_commit = ultimo_commit
        self.staged = [None]                                    #area de staged de la rama, donde se guardarán los archivos antes de commitearlos
    
    def nuevo_commit(self, ultimo_commit:Commit):               #función que actualiza el último nuevo commit cada vez que se cree uno nuevo
        self.ultimo_commit = ultimo_commit