from archivo import Archivo
from commit import Commit
from rama import Rama
class Repositorio:
    def __init__(self,):                      # constructor de la clase
        self.commit_anterior = None
        self.ram = [Rama("master")]           # lista de ramas del repositorio, la rama por defecto será "master"
        print("La rama master se ha creado exitosamente")
        self.ram_actual = self.ram[0]         # rama actual (HEAD) del repositorio, al crearlo será "master"
        self.historial = [[None, None, None]] # historial de los commits realizados en el repositorio   [[hash del commit, nombre de la rama, comentario del commit,]]

    
    def hacer_commit(self, comentario:str):             #función para crear un nuevo commit
        com = Commit(comentario, self.ram_actual.staged, self.commit_anterior)      #se crea el nuevo commit "com"
        self.ram_actual.nuevo_commit(com)               #se actualiza el último commit de la rama en la que se creo
        aux = [com.hash,self.ram_actual.nombre,com.cometario]   #Se crea una lista con los datos del commit para añadirlo al historial
        if self.historial[0][0] is None:                #Si el historial está vacio, se guardará en la posición [0]
            self.historial[0] = aux
        else:
            self.historial.append(aux)                  #Se añade el nuevo commit a la lista del historial
        print("Se ha creado el commit",com.hash,"en la rama",self.ram_actual.nombre)      #Confirmación del commit
        self.commit_anterior = com                      #se actualiza para que, al crear uno nuevo, este sea el anterior

    def crear_rama(self, nombre:str):               #Función para crear nuevas ramas en el repositorio
        nueva_rama = Rama(nombre, self.ram[0].ultimo_commit)    #creación de la rama
        self.ram.append(nueva_rama)                             #se añade la rama a la lista de ramas del repositorio
        print("La rama",nombre,"se ha creado exitosamente")     #confirmación
    
    def cambiar_rama(self, nombre:str):             #Función para cambiar de rama
        pos=-1                                      #variable que guardará la posición de la rama en la lista de ramas
        for k in range(len(self.ram)):              #Recorre todas los elementos de la lista de ramas
            if nombre == self.ram[k].nombre:        #si el nombre ingresado concuerda con el nombre de la rama en la posicion[k] se guarda k en la variable para luego ser utilizada
                pos=k
                break
        if pos!=-1:                                 #si se encontro una rama con el nombre ingresado
            self.ram_actual = self.ram[pos]         #se actualiza la rama actual a la rama que se cambiará
            print("Ahora estas posicionado en la rama",self.ram_actual.nombre)
        else:                                       #Si no se encuentra una rama con el nombre que se ingresó
            print("No existe alguna rama con el nombre:",nombre)
    
    def merge(self,nombre_rama:str):                            #función para hacer merge entre ramas
        if self.ram_actual.nombre == nombre_rama:               #si la rama ingresada es la misma en la que se encuentra actualmente, no se hará el merge
            print("No se puede realizar un Merge de la rama" + nombre_rama + ", pues te encuentras en ella")
        else:
            pos=-1                                              #variable que guardará la posición de la rama ingresada en la lista de ramas
            for k in range(len(self.ram)):
                if nombre_rama == self.ram[k].nombre:           #si el nombre ingresado concuerda con el nombre de la rama en la posicion[k] se guarda k en la variable para luego ser utilizada
                    pos=k
                    break
            if pos!=-1:                                         #si se encontro una rama con el nombre ingresado       
                nuevo_commit = Commit("Merge entre "+ self.ram_actual.nombre + " y " + self.ram[pos].nombre,self.ram_actual.staged,self.ram_actual.ultimo_commit) #se crea un nuevo commit producto del merge entre las dos ramas
                print("Se ha creado el commit",nuevo_commit.hash,"en la rama",self.ram_actual.nombre) #confirmación
                aux = [nuevo_commit.hash,self.ram_actual.nombre,nuevo_commit.cometario] #se crea una lista con los datos del commit creado para añadirlo al historial
                self.historial.append(aux)
                self.ram_actual.ultimo_commit = self.ram[pos].ultimo_commit #se actualiza el último commit de la rama a la que se le hizo el merge
                self.ram_actual.staged = self.ram[pos].staged       #se actualiza el área de staged de la rama a la que se le hizo el merge
                print("El Merge entre",self.ram_actual.nombre,"y",self.ram[pos].nombre,"se ha realizado exitosamente") #confirmación
            else:       #si pos == -1, entonces no se encontró ninguna rama con el nombre ingresado
                print("No existe alguna rama con el nombre:",nombre_rama)
    
    def mostrar_historial(self):                            #función para mostrar el historial de commits en el repositorio
        print("Historial de commits:")
        print("* ____Hash____  (Rama) comentario")          #Formato que utilizará
        for comm in reversed(self.historial):               #ciclo que pasa por cada elemento dentro de la lista de historial para mostrarlo por consola
            print("*",comm[0],"(",comm[1],") ",comm[2])