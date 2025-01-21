from archivo import Archivo
from commit import Commit
class Rama:
    def __init__(self, nombre:str, ultimo_commit:Commit = None):
        self.nombre = nombre
        self.ultimo_commit = ultimo_commit
        self.staged = [None]
    
    def nuevo_commit(self, ultimo_commit:Commit):
        self.ultimo_commit = ultimo_commit