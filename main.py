from repositorio import Repositorio
from archivo import Archivo

class main:
    def __init__(self):
        self.seguir = True
        self.iniciar = ""
        self.repo = None
    
    def iniciar_repo(self):
        while self.iniciar!="init":
            self.iniciar = input("Escriba init para inicializar un repositorio: ")       #se debe escribir "init" para empezar a utilizar el repositorio
        self.repo = Repositorio()            #se crea el repositorio

    def menu(self):                                             #función utilizada como menú para facilitar la interacción con el usuario
        while self.seguir:
            print("\nIndique la opcion a elegir: ")
            print("1. añadir un archivo al area de staged")                 #la función retornará True siempre que se escoja una opción distinta de 7, esto para poder continuar con los procesos hasta que el usuario así lo indique
            print("2. hacer un nuevo commit")
            print("3. crear una nueva rama")
            print("4. cambiar de rama")
            print("5. hacer un merge")
            print("6. mostrar el historial de commits")
            print("7. salir")
            eleccion=input("Escriba la operación a realizar: ")             #se guardará la opción seleccionada por el usuario
            match eleccion:
                case"1":                                               #caso 1, añadir un archivo al area de staged
                    nombre = input("Escriba el nombre del archivo: ")           
                    contenido = input("Escriba el contenido del archivo:\n")
                    arch = Archivo(nombre, contenido)                           #se crea un archivo
                    if self.repo.ram_actual.staged[0] is None:                       #si el área de staged está vacia se guarda en la posición [0]
                        self.repo.ram_actual.staged[0] = arch
                        print("Archivo subido exitosamente.")
                    else:
                        self.repo.ram_actual.staged.append(arch)                     #si no está vacia, se añade al área de staged
                        print("Archivo subido exitosamente.")
                    self.seguir = True                                 
                case"2":                             #caso 2, hacer un nuevo commit
                    nombre = input("Escriba el comentario del commit (recuerde ser descriptivo): ")
                    self.repo.hacer_commit(nombre)                   #se crea el commit
                    self.seguir = True
                case"3":                             #caso 3, crear una nueva rama
                    nombre = input("Escriba el nombre de la rama (recuerde ser descriptivo): ")
                    self.repo.crear_rama(nombre)                     #se crea la rama
                    self.seguir = True
                case"4":                             #caso 4, cambiar la rama en la que se está posicionado
                    nombre = input("Escriba el nombre de la rama a la que desea cambiar: ")
                    self.repo.cambiar_rama(nombre)                   #se cambia de rama actual
                    self.seguir = True
                case"5":                             #caso 5, hacer un merge entre la rama actual y la rama introducida
                    nombre = input("Escriba el nombre de la rama con la que se hará el Merge: ")
                    self.repo.merge(nombre)                          #se hace el merge si es posible
                    self.seguir = True
                case"6":                             #caso 6, muestra el historial de commits
                    self.repo.mostrar_historial()
                    self.seguir = True
                case"7":                             #caso 7, fin del programa
                    self.seguir = False
                case _:                                           #en caso de ingresar una opción fuera de las establecidas, volverá al menú y mostrará una advertencia
                    print("Opción invalida, vuelva a escribir su elección.")
                    self.seguir = True

principal = main()                      #Creación del objeto de clase main
principal.iniciar_repo()                #Inicio del repositorio, el bucle infinito termina cuando el usuario escriba "init"
principal.menu()                        #Menú de operaciones

print("Fin del programa.")              #FIN (Nelson Guerrero, 32067861, 305C1)