from repositorio import Repositorio
from archivo import Archivo

def menu():
    print("\nIndique la opcion a elegir: ")
    print("1. añadir un archivo al area de staged")
    print("2. hacer un nuevo commit")
    print("3. crear una nueva rama")
    print("4. cambiar de rama")
    print("5. hacer un merge")
    print("6. mostrar el historial de commits")
    print("7. salir")
    eleccion=input("Escriba la operación a realizar: ")
    if eleccion=="1":
        nombre = input("Escriba el nombre del archivo: ")
        contenido = input("Escriba el contenido del archivo:\n")
        arch = Archivo(nombre, contenido)
        if repo.ram_actual.staged[0] is None:
            repo.ram_actual.staged[0] = arch
            print("Archivo subido exitosamente.")
        else:
            repo.ram_actual.staged.append(arch)
            print("Archivo subido exitosamente.")
        return True
    elif eleccion=="2":
        nombre = input("Escriba el comentario del commit (recuerde ser descriptivo): ")
        repo.hacer_commit(nombre)
        return True
    elif eleccion=="3":
        nombre = input("Escriba el nombre de la rama (recuerde ser descriptivo): ")
        repo.crear_rama(nombre)
        return True
    elif eleccion=="4":
        nombre = input("Escriba el nombre de la rama a la que desea cambiar: ")
        repo.cambiar_rama(nombre)
        return True
    elif eleccion=="5":
        nombre = input("Escriba el nombre de la rama con la que se hará el Merge: ")
        repo.merge(nombre)
        return True
    elif eleccion=="6":
        repo.mostrar_historial()
        return True
    elif eleccion=="7":
        return False
    else:
        print("Opción invalida, vuelva a escribir su elección.")
        return True

iniciar=""
while iniciar!="init":
    iniciar = input("Escriba init para inicializar un repositorio: ")
repo = Repositorio()
seguir=True
while seguir:
    seguir=menu()
print("Fin del programa.")