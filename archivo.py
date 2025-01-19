class Archivo:
    def __init__(self, nombre:str,contenido:str):
        self.nombre = nombre
        self.contenido = contenido
    
    def mostrar(self):
        print("El archivo {0:10s} tiene el siguiente contenido:".format(self.nombre))
        print(self.contenido)

lista = [Archivo("texto1.txt","1234567890"),Archivo("texto2.txt","qwertyuiop"),Archivo("texto3.txt","asdfghjkl"),Archivo("texto4.txt","zxcvbnm,"),Archivo("texto4.txt","zsefcbhjuik,")]

