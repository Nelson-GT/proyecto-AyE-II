# Sistema Git Simulado con Programación Modular en Python
Elaborado por: Nelson Guerrero

## Clases:
- archivo : representación de un archivo real en python
- commit : conjunto de archivos que se guardan con un identificador único (hash)
- rama : Conjunto de commits creados con relación entre sí, pueden crearse distintas ramas en cualquier momento
- repositorio : Controlador de las ramas, tendrá las funciones básicas de git. Inicia con la rama "master"
- main : clase principal, tendrá el menú de usuario

## Como utilizar:
Primero, ejecute la clase main, le pedirá que escriba "init" para iniciar el repositorio, luego de eso, desplegará un menu de opciones en el cual el usuario podrá escoger la que necesite y trabajar en el repositorio.
Se aconseja crear un archivo antes de crear el primer commit
1. añadir un archivo al area de staged: crea un nuevo archivo y lo añade al área staged de la rama en la que se encuentre posicionado
2. hacer un nuevo commit: crea un nuevo commit, tendrá los archivos del área de staged de la rama en la que se cree, además tendrá un hash único conformado por 12 caracteres aleatorios entre [a,z] o [0,9]
3. crear una nueva rama: crea una nueva rama
4. cambiar de rama: cambia el HEAD a la rama que desee el usuario
5. hacer un merge: crea un nuevo commit producto de la fusión entre la rama actual en la que se encuentre, y la rama indicada por el usuario
6. mostrar el historial de commits: muestra todos los commits creados hasta el momento, su hash, la rama en la que se creó y su descripción 
7. salir: finalizará el programa
