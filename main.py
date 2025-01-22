from repositorio import Repositorio
from archivo import Archivo

def menu():                                             #función utilizada como menú para facilitar la interacción con el usuario
    print("\nIndique la opcion a elegir: ")
    print("1. añadir un archivo al area de staged")                 #la función retornará True siempre que se escoja una opción distinta de 7, esto para poder continuar con los procesos hasta que el usuario así lo indique
    print("2. hacer un nuevo commit")
    print("3. crear una nueva rama")
    print("4. cambiar de rama")
    print("5. hacer un merge")
    print("6. mostrar el historial de commits")
    print("7. salir")
    eleccion=input("Escriba la operación a realizar: ")             #se guardará la opción seleccionada por el usuario
    if eleccion=="1":                                               #caso 1, añadir un archivo al area de staged
        nombre = input("Escriba el nombre del archivo: ")           
        contenido = input("Escriba el contenido del archivo:\n")
        arch = Archivo(nombre, contenido)                           #se crea un archivo
        if repo.ram_actual.staged[0] is None:                       #si el área de staged está vacia se guarda en la posición [0]
            repo.ram_actual.staged[0] = arch
            print("Archivo subido exitosamente.")
        else:
            repo.ram_actual.staged.append(arch)                     #si no está vacia, se añade al área de staged
            print("Archivo subido exitosamente.")
        return True                                 
    elif eleccion=="2":                             #caso 2, hacer un nuevo commit
        nombre = input("Escriba el comentario del commit (recuerde ser descriptivo): ")
        repo.hacer_commit(nombre)                   #se crea el commit
        return True
    elif eleccion=="3":                             #caso 3, crear una nueva rama
        nombre = input("Escriba el nombre de la rama (recuerde ser descriptivo): ")
        repo.crear_rama(nombre)                     #se crea la rama
        return True
    elif eleccion=="4":                             #caso 4, cambiar la rama en la que se está posicionado
        nombre = input("Escriba el nombre de la rama a la que desea cambiar: ")
        repo.cambiar_rama(nombre)                   #se cambia de rama actual
        return True
    elif eleccion=="5":                             #caso 5, hacer un merge entre la rama actual y la rama introducida
        nombre = input("Escriba el nombre de la rama con la que se hará el Merge: ")
        repo.merge(nombre)                          #se hace el merge si es posible
        return True
    elif eleccion=="6":                             #caso 6, muestra el historial de commits
        repo.mostrar_historial()
        return True
    elif eleccion=="7":                             #caso 7, fin del programa
        return False
    else:                                           #en caso de ingresar una opción fuera de las establecidas, volverá al menú y mostrará una advertencia
        print("Opción invalida, vuelva a escribir su elección.")
        return True

iniciar=""
while iniciar!="init":
    iniciar = input("Escriba init para inicializar un repositorio: ")       #se debe escribir "init" para empezar a utilizar el repositorio
repo = Repositorio()            #se crea el repositorio
seguir=True                     #variable de control
while seguir:
    seguir=menu()               #se ejecuta el menú, en caso de seleccionar 7, retornara False lo que romperá el ciclo while(true)
print("Fin del programa.")      #FIN (Nelson Guerrero, 32067861, 305C1)