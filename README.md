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

### Ejemplo de uso:

Escriba init para inicializar un repositorio: init
La rama master se ha creado exitosamente

Indique la opcion a elegir:
1. añadir un archivo al area de staged
2. hacer un nuevo commit
3. crear una nueva rama
4. cambiar de rama
5. hacer un merge
6. mostrar el historial de commits
7. salir
Escriba la operación a realizar: 1
Escriba el nombre del archivo: texto1.txt
Escriba el contenido del archivo:
1234567890
Archivo subido exitosamente.

Indique la opcion a elegir:
1. añadir un archivo al area de staged
2. hacer un nuevo commit
3. crear una nueva rama
4. cambiar de rama
5. hacer un merge
6. mostrar el historial de commits
7. salir
Escriba la operación a realizar: 2
Escriba el comentario del commit (recuerde ser descriptivo): primer-commit
Se ha creado el commit 2ihk5h6kxah7 en la rama master

Indique la opcion a elegir:
1. añadir un archivo al area de staged
2. hacer un nuevo commit
3. crear una nueva rama
4. cambiar de rama
5. hacer un merge
6. mostrar el historial de commits
7. salir
Escriba la operación a realizar: 3
Escriba el nombre de la rama (recuerde ser descriptivo): develop
La rama develop se ha creado exitosamente

Indique la opcion a elegir:
1. añadir un archivo al area de staged
2. hacer un nuevo commit
3. crear una nueva rama
4. cambiar de rama
5. hacer un merge
6. mostrar el historial de commits
7. salir
Escriba la operación a realizar: 4
Escriba el nombre de la rama a la que desea cambiar: develop
Ahora estas posicionado en la rama develop

Indique la opcion a elegir:
1. añadir un archivo al area de staged
2. hacer un nuevo commit
3. crear una nueva rama
4. cambiar de rama
5. hacer un merge
6. mostrar el historial de commits
7. salir
Escriba la operación a realizar: 1
Escriba el nombre del archivo: texto2.txt
Escriba el contenido del archivo:
12345678900
Archivo subido exitosamente.

Indique la opcion a elegir:
1. añadir un archivo al area de staged
2. hacer un nuevo commit
3. crear una nueva rama
4. cambiar de rama
5. hacer un merge
6. mostrar el historial de commits
7. salir
Escriba la operación a realizar: 2
Escriba el comentario del commit (recuerde ser descriptivo): commit en rama develop
Se ha creado el commit imsh2vsheitt en la rama develop

Indique la opcion a elegir:
1. añadir un archivo al area de staged
2. hacer un nuevo commit
3. crear una nueva rama
4. cambiar de rama
5. hacer un merge
6. mostrar el historial de commits
7. salir
Escriba la operación a realizar: 4
Escriba el nombre de la rama a la que desea cambiar: master
Ahora estas posicionado en la rama master

Indique la opcion a elegir:
1. añadir un archivo al area de staged
2. hacer un nuevo commit
3. crear una nueva rama
4. cambiar de rama
5. hacer un merge
6. mostrar el historial de commits
7. salir
Escriba la operación a realizar: 5
Escriba el nombre de la rama con la que se hará el Merge: develop
Se ha creado el commit od68ktmv8pn7 en la rama master
El Merge entre master y develop se ha realizado exitosamente

Indique la opcion a elegir:
1. añadir un archivo al area de staged
2. hacer un nuevo commit
3. crear una nueva rama
4. cambiar de rama
5. hacer un merge
6. mostrar el historial de commits
7. salir
Escriba la operación a realizar: 6
Historial de commits:
* ____Hash____  (Rama) comentario
* od68ktmv8pn7 ( master )  Merge entre master y develop
* imsh2vsheitt ( develop )  commit en rama develop
* 2ihk5h6kxah7 ( master )  primer-commit

Indique la opcion a elegir:
1. añadir un archivo al area de staged
2. hacer un nuevo commit
3. crear una nueva rama
4. cambiar de rama
5. hacer un merge
6. mostrar el historial de commits
7. salir
Escriba la operación a realizar: 7
Fin del programa.