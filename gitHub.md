Descargamos git en https://git-scm.com/downloads

Utilizaremos la terminal Git Bash (se descarga cuando instalamos git)

1. Abrimos Git Bash
2. escribimos en la terminal lo siguiente: `git --version` 
(este nos mostrara el tipo de version q tenemos instalado)
3. Luego vamos a comenzar con la configuracion para ello escribimos: `git config --global user.name nombreDeUsuarioejemplo`
( La opcion --global es para que la config se efectue de manera global y no por proyecto. y en user.name configuramos git con nuestro nombre el q queramos )
.
4. escribimos: `git config --global user.email tuemail@gmail.com`
(Listo, ya realizamos la congiguracion inicial)

5. `git config --global core.editor "code --wait"` (esto sirve para configurar nuestro editor de texto VSCode, con esto señalamos q VSCode es nuestro editor de texto por defecto. Wait sirve para q espere a q cerremos el editor)

6. Si quisieramos ver nuestro archivo de config global escribimos: `git config --global -e`     //esto nos llevara a VSCode y nos mostrara la config

7. `git config --global core.autocrlf true`       (para Windows)
   `git config --global core.autocrlf input`      (para Mac/Linux)

 DATO: `git config -h` (muestras opciones para la config)

 COMANDOS BASICOS -- en la terminal
1) `ls`  //muestra todas las carpetas/directorios que tenemos

2) `pwd`  //nos dice en q carpeta/directorio nos encontramos

3) `cd nombreDeDirectorio`  //nos mueve a la carpeta seleccionada
NOTA: puedo abrir una carpeta dentro de otra: cd Desktop/carpeta1
Para salir de tal directorio: cd ..

NOTA 2: ejemplo de abrir una carpeta dentro de otra en la terminal
  cd Desktop
  ls (me muestra q carpetas hay en Desktop como -- Carpeta1 y Carpeta2)
  cd Carpeta1 (abre Carpeta1, y ahora estamos en Carpeta1)

4) `mkdir nombreDirectorio`  (esta funcion crea una carpeta con el nombre que deseamos)

5) `touch archivoNuevo`     --> Nos permite crear un archivo nuevo con el nombre que 
                                deseemos

6) `git init` (esto sirve para INICIALIZAR un repositorio dentro de la carpeta). Por ejemplo escribo: git init (luego presiono enter y me va a aparecer -> Initialized empty Git repository in C:/Users/Usuario/Desktop/Carpeta1/.git/   <-- .git me indica que este directorio esta oculto, no se mostrara lo q hay en .git si escribo ls. Pero si lo hara con "ls -a" >)


### FLUJO DE TRABAJO CON GIT  

**git add** : cuando ejecutamos este comando, lo que haremos sera seleccionar los archivos que queramos pasar a la etapa Stage. En esta Etapa basicamente se considera los cambios/actualizaciones del archivo que queramos subir al repositorio (pero no se suben al repositorio).

**git commit** : sube el archivo en la etapa commit (es la etapa despues de stage, es decir confirma que quiero guardar este cambio para luego pasarlo al repo).

OTROS COMANDOS:
En Git Bash escribo lo siguiente:

1. `code .`  //esto abre mi editor de texto (q por defecto es VSCode) dentro de la carpeta/directorio donde estoy

2. `git status`  //no muestra el estado actual de nuestro repositorio "Untracked files:" me muestra los archivos q no se subieron (o puedo subir)

3. `git add nombreDeArchivo` 
//con este comando preparo el archivo a subir a mi repositorio
Luego puedo verificar el estado de mi repo. con git status , nos aparecera algo como "Changes to be committed:" ahi me muestra los archivos en etapa de Stage.

NOTA: para subir mas de un archivo escribimos por ejemplo: *git add archivo1 archivo2*    //respetando los espacios
En caso de modificar un archivo como archivo2 (es decir hicimos cambios del codigo desde VScode), tendremos que **actualizar** estos cambios a mi etapa stage => vuelvo a escribir: *git add archivo2*

4. `git commit -m "mensaje entre comillas"`  //esto es para confirmar los cambios a subir.

5) `rm nombreDeArchivo`  //rm es un comando q sirve para eliminar un archivo
ejemplo: rm archivo2
         git status  //verifico su estado y me aparece "deleted:  archivo2"
         git add archivo2  //lo paso a la etapa Stage
         git commit -m "eliminar archivo 2" //esto elimina el archivo2 de todas las etapas (stage y commit)

**otra forma** mas corta es: git rm archivo2
                             git commit -m "eliminar archivo 2"
                             
6) si quiero restaurar un archivo a eliminar que pase a la etapa Stage (justo antes de comitear) utilizo:
 
`git restored --stage nombreArchivo`

ejemplo: git restored --staged archivo2
En caso de que quiera descartar los cambios y que lo devuelva a mi lista ls escribo:
      git restore archivo2

7. `git push`  :sube lo commiteado al repo. remoto


## ***CONECTANDO CON GITHUB***:
1. Creamos una cuenta 
2. Luego creamos un repositorio

ABRIMOS **Git Bash** :
3. Y escribimos lo siguiente (esto lo hacemos despues de haber "commiteado los archivos")

`git remote add origin https://github.com/ejemplo`    

//esta url lo encontramos en la opcion <>Code (que se haya dentro del repositorio que cree). 

4. Siguiente a eso:

`git push -u origin main`

//main es una rama que por defecto se crea en nuestro repo.
Presiono Enter, y nos aparece:

Username for 'https://github.com': NombreDeUsuarioDeGit  //luego ENTER

Password for 'https://ejemplo@gmail.com': contraseñaToken  //esta contraseñaToken lo conseguimos desde nuestra cuenta GITHUB 1)Desde el icono de nuestra cuenta seleccionamos la opcion settings .2)Luego bajamos y presionamos "<> Developer settings" 3) pincho en "Personal access tokens" 4) luego en "Personal access tokens (classic)" -> "Generate new Token" -> "Generate new Token (classic)" 5) en "note" escribimos el nombre que quiera ponerle a mi token y en "Select scopes" selecciono la opcion "repo" 6) Por ultimo bajo y pincho en <Generate Token> 
7) copio el token y lo reemplazo en "constraseñaToken" (de la terminal)

NOTA: este token dura 30dias o mas depende de la opcion q elijamos a la hora de crearla

5. Enter y Listo! , el codigo se subio a la repo.


**RAMAS EN GIT o BRANCHES**
Notar que en nuestra terminal nuestra rama se llama por defecto "master" entonces en mi caso el paso 4. de ***CONECTANDO CON GITHUB*** no me funciono. (Esto pasa porque por defecto de github nuestra rama del repo se llama "main")

`git branch`   :me dice en que rama me encuentro, y cuales hay.

`git checkout -b nameDeRamaNueva`  : crea una nueva rama

`git checkout nombreDeRama`    :Cambia a la rama que yo quiero utilizar.

`git log --oneline`    :me da el historial de los cambios en mi rama

`cat nameArchivo`    :me muestra el contenido de un archivo.

`git merge nombreOtraRama`   :sirve para pasar los cambios de otra rama a mi rama principal (debo situarme ahi)

`git branch -d nombreRamaAEliminar`   :elimina de forma local una rama (para llo debemos situarno en otra rama)

`git push origin --delete nombreRamaAEliminar`  :sube los cambios al repo.remoto     


**REPOSITORIOS REMOTOS Y LOCALES**

REMOTO : lo que se sube a gitHub ejemplo

LOCAL : lo que se crea dentro de los comandos en git

`git remote -v`  -> indica las conexiones remotas que tiene nuestro proyecto local

`git remote set-url origin urlDemiRepoRemota`   -> Para cambiar la URL de tu repositorio remoto en Git tan solo    
                                  escribimos el siguiente código agregando la nueva dirección


NOTA: git pull --rebase urlDemiRepoRemoto
En lugar de utilizar git merge para integrar la rama remota en la local, usa git rebase. Me ayudo a actualizar los cambios de mi rama remota a la local y viceversa.

**¿Cómo eliminar un repositorio de Git creado con ‘git init’ en un directorio?**
`rm -rf .git`
