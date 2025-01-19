from archivo import Archivo
from commit import Commit
from rama import Rama
class Repositorio:
    def __init__(self,):
        self.rama = None
        self.staged = lista = [Archivo("texto1.txt","1234567890"),Archivo("texto2.txt","qwertyuiop"),Archivo("texto3.txt","asdfghjkl"),Archivo("texto4.txt","zxcvbnm,"),Archivo("texto4.txt","zsefcbhjuik,")]
        self.commit_anterior = None
        self.ram = [Rama("master")]
        self.ram_actual = self.ram[0]
        self.historial = [[None, None, None]] # [[hash del commit, nombre de la rama, comentario del commit,]]

    
    def hacer_commit(self, comentario:str):
        com = Commit(comentario, self.staged, self.commit_anterior)
        self.ram_actual.nuevo_commit(com)
        aux = [com.hash,self.ram_actual.nombre,com.cometario]
        if self.historial[0][0] is None:
            self.historial[0] = aux
        else:
            self.historial.append(aux)
        print("Se ha creado el commit",com.hash,"en la rama",self.ram_actual.nombre)
        self.commit_anterior = com

    def crear_rama(self, nombre:str):
        nueva_rama = Rama(nombre, self.ram[0].ultimo_commit)
        self.ram.append(nueva_rama)
        print("La rama",nombre,"se ha creado exitosamente")
    
    def cambiar_rama(self, nombre:str):
        pos=-1
        for k in range(len(self.ram)):
            if nombre == self.ram[k].nombre:
                pos=k
                break
        if pos!=-1:
            self.ram_actual = self.ram[pos]
            print("Ahora estas posicionado en la rama",self.ram_actual.nombre)
        else:
            print("No existe alguna rama con el nombre:",nombre)
    
    def merge(self,nombre_rama:str):
        if self.ram_actual.nombre == nombre_rama:
            print("No se puede realizar un Merge de la rama" + nombre_rama + ", pues te encuentras en ella")
        else:
            pos=-1
            for k in range(len(self.ram)):
                if nombre_rama == self.ram[k].nombre:
                    pos=k
                    break
            if pos!=-1:
                self.ram_actual.ultimo_commit = self.ram[pos].ultimo_commit
                print("El Merge entre",self.ram_actual.nombre,"y",self.ram[pos].nombre,"se ha realizado exitosamente")
            else:
                print("No existe alguna rama con el nombre:",nombre_rama)
    
    def mostrar_historial(self):
        for comm in reversed(self.historial):
            print("*",comm[0],"(",comm[1],") ",comm[2])




