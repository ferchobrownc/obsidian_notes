Para iniciar la conexión, se accede al host `bandit.labs.overthewire.org` a través del puerto `2220`  utilizando el protocolo **ssh**

![](imgs/ssh.png)
## 🔥LEVEL 0  - user:`bandit0`  🔑 password: `bandit0`
- **Objetivo general**: encontrar el password para el siguiente nivel
- **Comando usados**: `ls, cat`

Accedemos al nivel inicial con las credenciales proporcionadas por la plataforma Bandit: usuario:  bandit0  y la contraseña: bandit0.

Una vez dentro, ejecutamos el comando `ls` para listar los archivos disponibles  en el directorio. A continuación, utilizamos el `cat`para visualizar el contenido del  fichero.
![](imgs/level0.png)
![](imgs/level0-1.png)

## 🔥LEVEL 1 - user: `bandit1` 🔑 password: `ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If`
- **Objetivo:** encontrar el password para el siguiente nivel
- **Comando usados**: ' ls, cat '

Tras acceder con este usuario, se ejecuta el comando `ls` para listas los archivos del directorio actual, donde se identifica un archivo cuyo nombre comienza con un  guion `"-"` (conocido como **dashed filename** ). En sistemas  Linux, los archivos cuyo nombre empiezan con `-` pueden confundirse con opciones de comando,  por lo que debemos usar rutas relativas al ejecutarlos o manipularlos correctamente. En este caso, para visualizar el contenido del archivo  mencionado se utiliza  `cat ./-`, de esta manera, se garantiza que el intérprete trate como un nombre de archivo y no como argumento, permitiendo mostrar correctamente su contenido.

![](imgs/bandit1-1.png)

## 🔥LEVEL 2 - user: bandit1 🔑 password: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx
- **Objetivo:** encontrar el password para el siguiente nivel
- **Comando usados**: ' ls, cat '
 Tras  acceder  a este nivel, se ejecuta el comando `ls`, como resultado se identifica un archivo llamado `--spaces in this filename--`,  este archivo tiene dos particularidades,  comienza por '--',  y contiene tiene espacios. Al intentar visualizar su contenido con  `cat`, no se obtine el resultado esperado, ya que el intérprete puede confundir el nombre del archivo con opciones del comando, además de verse afectado por los espacios en el nombre.
  Por consiguiente, para solucionar este problema, es necesarios escapar correctamente el nombre del archivo, existen varias formas de hacerlo:
 - con comillas dobles ´"` 
 - con comillas simples  '`
 - con `\`antes de cada espacio del nombre del archivo
Todas estas formas debemos usar rutas relativas al ejecutarlos o manipularlos y así visualizar el contenido del archivo correctamente.

![](imgs/bandit2-1.png)
Notas :
- Los espacios en nombres de archivo deben ser tratados cuidadosamente en la terminal
- El uso de comillas o caracteres de escape es fundamental para evitar errores de interpretación.
##  🔥LEVEL 3 - user: bandit3 🔑 password: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
- **Objetivo:** encontrar el password para el siguiente nivel
- **Comando usados**: ' ls, cd, cat '
 
![](imgs/bandit3-1.png)

Tras acceder a este nivel, se ejecuta el comando `ls` para listar todos los archivos del directorio actual. Se identifica un directorio llamado `inhere`, por lo que  nos movemos a él con el comando `cd`. A continuación, ejecutamos el comando `ls`para listar los archivos; como resultado, el directorio esta vacío. Por ello, procedemos a ejecutar el comando `ls -la` para listar todos los archivos, incluso los ocultos. De esta forma,encontramos  un archivo oculto llamado `...Hiding-Fom-You`. Finalmente, utilizamos el comando `cat` para visualizar su contenido: `cat ...Hiding-From-You`. 

![](imgs/bandit3-1.png)
## 🔥LEVEL 4- user: bandit4  🔑password: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
- **Objetivo:** encontrar el password para el siguiente nivel
- **Comando usados**: ' ls, cd, find, cat '

 Tras acceder a este nivel,  ejecutamos el comando `ls`para listar los archivos, nos encontramos con el directorio`inhere`, accedemos con el comando `cd`, ejecutamos nuevamente `ls`, como resultado tenemos varios archivos. Necesitaremos buscar que tipo de archivo es de texto, de esta manera sabremos cual abrir, así no tendremos que ver cada archivo de forma manual. 
 
 Procedemos a ejecutar el siguiente comando: `find . -type f -exec {} \ ; ` Este comando recorre de forma re cursiva el directorio actual y todos los sub-directorios. Cada vez que encuentra un archivo, ejecuta el comando `file`sobre él, mostrando como resultado el tipo de cada archivo. De esta manera sabremos que archivo contiene tipo texto, luego ejecutamos un `cat`para ver su contenido.
![](imgs/bandit4-1.png)
Explicamos detalladamente el comando anterior:

| Comando       | Explicación                                                                                                                               |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **find**      | Es una herramienta de Linux que permite buscar archivos y directorios dentro de una ruta especifica.                                      |
| **.** (punto) | Indica que la búsqueda se realizará en el directorio actual.                                                                              |
| **-type f**   | Filtra los resultados para mostrar únicamente archivos (excluyendo directorios)                                                           |
| **-exec**     | Permite ejecutar un comando sobre cada archivo encontrado                                                                                 |
| **file**      | Es el comando que se ejecutará sobre cada archivo. Su función es identificar el tipo de archivo (texto, binario, etc.)                    |
| **{}**        | Representa cada archivo encontrado durante la búsqueda. Es un marcador que `find`sustituye automáticamente por el nombre de cada archivo. |
| **\ ; **      | Indica el final del comando que se ejecuta con `-exec`. La barra invertida (`\`) es necesaria para escapar el punto y coma.               |
##  🔥LEVEL 5- USER: bandit5 🔑password: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
- **Objetivo** : Encontrar la password del siguiente nivel
- **Comando utilizados**: `ls, cd, find, xargs, cat `

Tras ingresar a este nivel, ejecutamos un `ls` para listar los archivos del directorio. Como resultado, se obtiene el archivo con nombre `inhere`; a continuación ejecutamos el comando `cd`para acceder a dicho directorio,  dentro encontramos una gran cantidad de arhivos, por lo que no resulta efiiente revisar uno por uno, ya que sería un proceso muy extenso. Para ello, nos apoyamos  en las pistas proporcionadas para este nivel, las cuales son:
- **human-redeable**: se refiere a datos o formatos de información, como texto en lenguaje natural (ASCII/Unicode).
- **1033 bytes**: indica el tamaño exacto del archivo que debemos encontrar.
- **not-executable**: se refiere a un archivo que no puede ejecutarse como un programa, es decir que contine datos.

Con  base en estas pistas procedemos a realizar una búsqueda utilizando el siguiente comando: `find . -size 1033c | xargs cat`

  Explicamos el anterior comando a continuación 

| Comando       | Explicación                                                                                      |
| ------------- | ------------------------------------------------------------------------------------------------ |
| **find**      | es un comando para buscar archivos y directorios                                                 |
| **.** (punto) | indica que la busqueda se realizara en el directorio actual y dentro de todos sus subdirectorios |
| **-size**     | filtra por el tamaño                                                                             |
| **1033c**     | se especifica que son bytes con la letra `c` (`k`para kilobytes, `m`para megabytes)              |
| **\|** (pipe) | se usa para conectar comandos                                                                    |
| **xargs**     | toma entradas y las convierte en argumentos para otro comando                                    |
| **cat**       | muestra el contenido de archivos en la terminal                                                  |
|               |                                                                                                  |
![](imgs/bandit5.png)

## 🔥Level 6 - user bandit6 🔑password: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
- **Objetivo:** encontrar la password para el siguiente nivel
- **Comandos utilizados:**  `ls, cd, find, 2>/dev/null, grep, xargs`
Tras el ingreso a este nivel, nos apoyamos de las pistas que nos proporcionan para el mismo, las cuales son las siguientes:
- **owned by user bandit7:**  el archivo debe  pentenecer al usuario `bandit7' 
- **owned by group bandit6:** el archivo debe  pertenecer al grupo `bandit6`
- **33 bytes in size**: el archivo tiene un tamaño exacto de `33 bytes`
Con base a estas características, no es eficiente buscar manualmente entre todos los archivos. Por ello, utilizamos el comando `find`que nos permite filtrar archivos según distintos criterios. Procedemos a ejecutar el siguiente comando 
-  `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null | xargs cat`
Nos aposllamos del comando `2>/dev/null`, de esta manera redirigimos los errores del comando. Esto permite ocultar mensajes de error, como los de permisos denegados, y mostrar únicamente los resultados relevantes.

Explicamos los comandos utilizados:

| Comando            | Explicación                                                              |
| ------------------ | ------------------------------------------------------------------------ |
| **find**           | comando para buscar archivos y directorios                               |
| **/**              | busca desde el directorio raíz                                           |
| **-user bandit7**  | filtra archivos pernecientes al usuario `bandit7`                        |
| **-group bandit6** | filtra archivos del grupo `bandit6`                                      |
| **-size 33c**      | selecciona los archivos de tamaño `bytes` (para eso usamos la letra `c`) |
| **2**              | representa el fluo de errores (stderr)                                   |
| **>**              | indica una redirección                                                   |
| **/dev/null**      | es un archivo especial que actúa como un "agujero negro"                 |
| **\|** ()          | se usa para conectar comandos                                            |
| **xargs**          | toma entradas y las convierte en argumentos para otro comando            |
| **cat**            | muestra el contenido de archivos en la terminal                          |

![](bash/OverTheWire/imgs/bandit6.png)
## 🔥Level 7 - user bandit7 - 🔑password morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
- **Objetivo:** Encontrar la password del siguiente nivel
- **Comandos utilizados:** `cat, grep`
Tras acceder a este nivel, nos apoyamos de la pista proporcionada del mismo, la cual nos indica que la contraseña se encuentra en un archivo llamado `data.txt`, específicamente en la línea que contiene la palabra `millionth`. Para localizarla  ejecutamos el comando `cat data.txt | grep millionth`
- con el comando `cat data.txt` nos muestra el contenido del archivo
- `|` -> redirige la salida del primer comando hacia el segundo. 
- `grep millionth` -> filtra y muestra únicamente las líneas que contienen la palabra `millionth`
cat data.txt | grep millionth
![](imgs/.png)
Podemos simplificar este comando, de esta manera podemos optimizar recursos y velocidad con el siguiente comando: `grep millionth data.txt`
- el `grep`realiza una búsqueda línea por línea en el archivo `data.txt`, busca si aparece la palabra `millionth` y al encontrar  una coincidencia imprime esa linea completa en pantalla.
![](imgs/-1.png)

## 🔥 Level 8 - user bandit8 🔑password dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
- **Objetivo:** Encontrar la password del siguiente nivel.
- **Comando utilizados:** `ls, sort, uniq -u  
Tras acceder al nivel,  ejecutamos un `ls` para listar el contenido de los archivos del directorio. Basándonos en las pistas proporcionadas, se nos indica que la contraseña se encuentra en un archivo con nombre `data.txt`el cual identificamos después  de ejecutar dicho comando. 

A continuación, utilizamos el siguiente comando para encontrar la información única dentro del archivo: 
`sort data.txt | uniq -u
El comando `sort` ordena alfabéticamente  el contenido del archivo `data.txt`. Esto es importante ya que el comando `uniq` solo funciona correctamente cuando las líneas idénticas están juntas.
Por su parte `uniq -u` muestra únicamente las lineas que aparecen una sola vez en el archivo. Es decir, ignora todas las líneas repetidas y devuelve únicamente aquella que no se repite.   

![](-2.png)
##  🔥 Level 9 - user bandit 9 🔑password 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

- **Objetivo:** Encontrar la password del siguiente nivel.
- **Comandos utilizdos:** `ls, strings, grep`

Tras acceder a este nivel, las pistas  indican que la contraseña se encuentra dentro de un archivo llamado `data.txt`,    junto a varios caracteres `=`. 
Primero ejecutamos el comando `ls`para listar los archivos del directorio. En la salida encontramos el archivo antes mencionado (`data.txt`).
A continuación, ejecutamos el siguiente comando para buscar posibles cadenas de texto relevantes  dentro del archivo: `strings data.txt | grep "==="` 
- El comando `strings data.txt` extrae todas las cadenas de texto legibles contenidas en el archivo, incluso si este es binario. 
- Con `grep "==="`filtramos únicamente las lineas que contienen el caracter `=`.
Esto nos permite localizar la contraseña dentro del archivo.
![](-3.png)


##   🔥 Level 10 - user bandit10 🔑password FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
- **Objetivo**: Encontrar la password para el siguiente nivel.
- **Comandos utilizados:** `ls, cat, base64`

Tras acceder  a este nivel, siguiendo las pistas proporcionadas, las cuales nos indican que la contraseña se encuentra en un archivo con nombre `data.txt` esta se encuentra codificada en `base64`, procedemos a  ejecutar el comando `ls` para listar los archivos del directorio,  como salida obtenemos el archivo `data.txt`, a continuación ejecutamos el comando `cat data.txt `para ver su contenido, luego verificamos si esta codificado con el comando `base64 -d data.txt`
- `base 64`: es un método de codificación que convierte datos binarios en una cadena de texto ASCII, para asegurar la integridad de los datos al transportarlos por medios que solo manejan texto.
- `-d`: esta opción significa "decode" el cual decodifica el contenido del archivo, lo cual nos permite leer el contenido del archivo correctamente, obteniendo la contraseña para el siguiente nivel. 

![](-4.png)

##  🔥Level 11 - bandit11 - 🔑password dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
- **Objetivo:** Encontrar la password para el siguiente nivel.
- **Comandos utilizados:** `ls, cat,  
Tras acceder a este nivel, nos apoyamos de las pistas que nos brindan, las cuales nos dice que la contraseña se almacena en archivo con nombre `data.txt`, donde todas las letras minúsculas (a-z) y mayúsculas (A-Z) han sido rotadas por 13 posiciones (`rot13`). 
También nos brindan un material de lectura, en el cual podemos ver la explicación de `rot13`: es un cifrado de César utilizado para ocultar un texto sustituyendo cada letra por la letra que está trece posiciones por delante del alfabeto. `A`se convierte en `N`, `B`se convierte en `O`y así hasta la `M`, que se convierte en `Z`. Luego la secuencia se invierte: `N`se convierte en `A`, `O` se convierte en `B`y así hasta la `Z`, que se convierte en `M`. 
Con esto comprendemos su uso, procedemos: 
ejecutar el comando para listar los archivos del directorio
`ls` 
como salida tenemos el archivo 
`data.txt` 
A continuación ejecutamos 
`cat data.txt` 
para ver el contenido del archivo, observamos que no se puede entender ya que esta en desorden
A continuación, ejecutamos 
`cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-n'`
como salida tenemos el archivo decodificado pudiendo así ver la contraseña con éxito.
![](imgs/bandit11.png)
##  🔥Level 12- bandit12 -🔑 password: 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
- **Objetivo:** Encontrar la password para el siguiente nivel. 
- **Comandos utilizados:** `ls, gzip, xxd, gzip2, tr, file, head, cat' 

 En este nivel la cosa se pone interesante. Nos dicen que la contraseña está dentro de un archivo en formato **hexdump**, pero no es tan simple: está comprimido varias veces en distintos formatos.

Además, el archivo (`data.txt`) se encuentra en un directorio con permisos de solo lectura, así que no podemos trabajar directamente sobre él.

### 🛠 Preparando el entorno

Primero listamos los archivos:

`ls -l`

Vemos que `data.txt` solo tiene permisos de lectura. Para poder manipularlo, creamos un directorio temporal en `/tmp`, ya que ahí sí tenemos permisos de ejecución:

`mktemp -d ` 
`cd /tmp/<directorio>`

Copiamos el archivo:

`cp ~/data.txt . ` 
`mv data.txt datahex`

### 🔍 Identificando el archivo

Revisamos el contenido:

`head datahex`

Aquí vemos los bytes `1f 8b 08`, lo que nos da una pista clara: es un archivo comprimido en **gzip**, pero en formato hexdump.

Convertimos el archivo a binario:

`xxd -r datahex datacompres`

Ahora sí podemos empezar a trabajar con él.

### 🔄 Proceso de descompresión

A partir de aquí, el flujo es bastante repetitivo:

1. Identificar el tipo de archivo:

`file datacompres`

2. Cambiar la extensión según corresponda
3. Descomprimir con la herramienta adecuada

Ejemplo:

`mv datacompres datacompres.gz `
`gzip -d datacompres.gz`

Luego:

`file datacompres`

Y así sucesivamente con **bzip2** y **tar**:

`mv datacompres datacompres.bz2`  
`bzip2 -d datacompres.bz2`  
  
`tar -xf datacompres`

### 🔁 Nota personal

Aquí básicamente es repetir el mismo proceso varias veces.  
Puede parecer tedioso, pero la clave es **no perderse**: siempre verificar con `file` antes de hacer el siguiente paso.

### 🧩 Resultado final

Después de varias iteraciones de descompresión, finalmente obtenemos un archivo en formato **ASCII**.

Lo abrimos:

`cat data8`

Y listo — ahí está la contraseña del siguiente nivel.

### 💡 Aprendizaje clave

- Saber identificar tipos de archivo con `file`
- Entender firmas de archivos (como `1f 8b 08` para gzip)
- Manejo básico de compresión: `gzip`, `bzip2`, `tar`
- Paciencia y método → este nivel es más de proceso que de dificultad técnica
![](imgs/bandit12.png)

##  🔥Leven 13 - bandit13 - password: FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
- **Objetivo:** Encontrar la password para el siguiente nivel
-  **Comandos utilizados**: `ls, chmod, ssh, cat, scp`

### Descripción:

En este nivel  nos indican que la contraseña para el siguiente nivel se encuentra en 
`/etc/bandit_pass/bandit14`
Sin embargo, no tenemos permisos para leer este archivo directamente. En su lugar disponemos de una clave privada SSH que nos permitirá autenticarnos como el usuario `bandit14`.

### Enumeración

Listamos los archivos disponibles:
`ls`
Se identifican dos archivos:
- `HINT`: contiene instrucciones para el nivel.
- `sshkey.private`: clave privada SSH que utilizaremos para autenticarnos.
### Extracción de la clave privada

Para ello procedemos a salir del nivel ya que en el laboratorio no tenemos permisos para poder conectarnos al servidor.
Para copiar la clave a nuestra máquina local, utilizamos **scp** que funciona sobre **SSH**: 
`scp -P 2220 bandit13@bandit.labs.overthewire.org:sshkey.private .`
Este comando descarga el archivo  `sshkey.private`al directorio actual de nuestra máquina local de forma cifrada.

### Ajustes de permisos

Antes de usar la clave, es necesario restringir sus permisos para que **OpenSSH** la acepte:
`chmod 600 sshkey.private`
Esto garantiza que solo el usuario actual tenga acceso al archivo, evitando que SSH rechace la clave por motivos de seguridad.

Ahora utilizamos la clave privada para autenticarnos como `bandit14` 
`ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220`
- `-i sshkey.private`: especifica la clave privada
- `-p 2220`: indica el puerto correcto
![](imgs/bandit13-1.png)
### Obtención de la contraseña

Una vez dentro como `bandit14`, ya tenemos permisos para leer la contraseña:
`cat /etc/bandit_pass/bandit14`
Esto nos devuelve la contraseña del  nivel 14
![](imgs/bandit13_pass14-1.png)
## 🔥 Level 14 - bandit14 - password: MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
- **Objetivo:** Encontrar la password para el siguiente nivel.
- **Comandos utilizados:** `cat, nc`
En este nivel se nos indica que la contraseña del siguiente nivel puede obtenerse enviando la contraseña actual a un servicio que escucha en el peurto `30000` en `localhost`.

### 🔑Acceso al nivel

El acceso puede realizarse mediante:
- Contraseña obtenida en el nivel anterior
- Utilizando la clave privada SSH obtenida previamente
### 🔌 Conexión 
Para interactuar con el servicio utilizamos Netcat, es una herramienta que permite establecer conexiones TCP/UDP:
`nc localhost 30000`
Este comando establece una conexion con el servicio local que está escuchando en el puerto `30000`

### Envio de la contraseña
Una vez establecida la conexion, se introduce la contraseña del nivel actual:
`MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS`
El servicio valida la contraseña y devuelve como respuesta la contraseña del siguiente nivel. 

### Resultado
Tras enviar la contraseña correctamente, el servidor responde con la contraseña del nivel `bandit15`
![](imgs/bandit14-1.png)

##  🔥Level15 - bandit15 - 🔑password: 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
- **Objetivo:** encontrar la password para el siguiente nivel.
- **Comandos utilizados:** `openssl, printf`
### Descripción 
En este nivel nos dicen que la contraseña para el siguiente nivel se encuentra en el puerto `30001` en `localhost`y que la conexión debe realizarse  utilizando `SSL / TLS `

### Análisis 
Normalmente, para conectarse a un puerto se puede usar  `nc`(netcat). Sin embargo, este caso especifica que la conexión utiliza **SSL** por lo que `nc`no funcionara correctamente porque no soporta SSL/TLS, por lo que no puede completar el handskake necesario con el servidor. 
Para interactuar con servicios **SSL** desde la terminal se puede utilizar `openssl `, específicamente el modo `s_client`, que permite actuar como un cliente **SSL/TLS**
### Solución  
Se establece conexión con el servidor usando  el comando
`openssl s_client -connect localhost:30001`
Una vez conectados, se envía la contraseña del nivel actual. 
El servidor responde con la contraseña del siguiente nivel.

Este proceso también se puede automatizar usando: 
`printf "8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo\n" | openssl s_client -connect localhost:30001 -quiet`
Explicación:
- `printf`: envía la contraseña seguida de un salto de linea `\n`, simulando la pulsación ENTER.
-  `| `(pipe) este operador redirige la salida de **printf** como entrada para openssl
- `openssl s_client`: establece una conexión SSL/TLS con el servidor.
- `-quiet`: elimina la información innecesaria, mostrando únicamente la respuesta del servidor. 

![](imgs/bandit15.png)
## 🔥Level16 - bandit16 - 🔑password: kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
- **Objetivo:** encontrar la password para el siguiente nivel 
- **Comandos utilizados:** `nc, openssl, nano, chmod`

### Descripción 
En este nivel nos cuentan que la contraseña se encuentra en un puerto en `localhost`con rango de `31000 a 32000`el cual utiliza  SSL/TLS.

### Análisis 
Al tener un rango de puertos tan grande debemos realizar un escaneo con una herramienta, en este caso utilizaremos `nmap ` la cual es un herramienta de escaneo de redes y puertos.

### Escaneo
Utilizamos nmap:
`nmap -sV -vvv --open -p 31000-32000 localhost `
- `-sV`: prueba los puertos abiertos y detenermina el servicio e información de la versión 
- `-vvv`: nos muestra lo que esta haciendo 
- `--open`: muestra solo los puertos abiertos
- `-p 31000-32000`: el rango de puertos donde debe buscar
- `localhost`: en la ip local 
Luego obtendremos los puertos abiertos que estan a la escucha en localhost, tambien los servicios, en el cual nos encontramos el puerto ` 31518/tcp open ssl/echo`y el puerto `31790/tcp open ssl/unknown`, luego de leer ambos, nos quedamos solo con el puerto `31790` ya que el servicio `ssl/echo` solo devuelve la misma entrada que le enviamos, mientras que el servicio `ssl/unknown `nos puede ofrecer una respuesta diferente, lo que indica que puede contener la solución del nivel. 

![](imgs/bandit16_nmap.png)

Tambien podemos usar: 
`nc -zv localhost 31000-32000`
Luego verificar conexión con cada puerto.

### Verificación
Luego de haber obtenido el puerto correcto, procedemos a verificar
`printf "kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx\n" | openssl s_client -connect localhost:31790 -quiet `
El uso de `printf`permite automatizar el envío de la contraseña, evitando la interacción manual durante la conexión SSL.
Obtenemos una **RSA PRIVATE KEY**, la cual procedemos a copiar a un archivo en la máquina local para poder utilizarla con SSH de forma segura, creamos el archivo con el comando `nano bandit16.key`  y pegamos el contenido. 
Cambiamos sus permisos para el que el servidor la reconozca y no de fallos, con el comando `chmod 600 bandit16.key`  y ya tendríamos la llave para ingresar al siguiente nivel, de esta manera damos por terminado el nivel.

### Obtención contraseña
Accedemos al siguiente nivel con la clave privada
`ssh -i bandit16.key bandit14@bandit.labs.overthewire.org -p 2220`
procedemos a buscar la contraseña en `cat /etc/bandit_pass/bandit17` de esta manera ya tenemos la contraseña para guardarla y la clave privada. 
![](imgs/bandit16_pass17.png)

## 🔥Level17 - bandit17 - 🔑password: EReVavePLFHtFlFsjn3hyzMlvSuSAcRD
- **Objetivo:** encontrar la password para el siguiente nivel. 
- **Comandos utilizados:** 

### Análisis 
En este nivel tenemos dos archivos en el mismo directorio, `passwords.old`y `passwords.new` La contraseña para el siguiente nivel están en el archivo `passwords.new`y está en la única linea que se ha cambiado entre estos dos archivos. 

### Obtención Clave
Ejecutamos el comando 

`diff passwords.old passwords.new | grep ">"`
- `diff` nos permite comparar ambos archivos línea por línea 
- `| `conecta  la salida con otro comando 
- `grep ">"` filtra la línea correspondiente al archivo nuevo.  
como salida obtendremos la contraseña del siguiente nivel
![](imgs/bandit17.png)


## 🔥Level18  - bandit18 - 🔑password: x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
- **Objetivo:**  encontrar la password para el siguiente nivel 
- **Comandos utilizados:** `cat, ls, ssh`

### Análisis
La contraseña se encuentra en un archivo llamado `readme`en el directorio personal (home).
Sin embargo, al intentar acceder por SSH, la sesión se cierra inmediatamente. Esto se debe a que el archivo `.bashrc`  ha sido modificado para cerrar la sesión inmediatamente al iniciar, lo que impide acceder de formar interactiva.
El archivo `.bashrc`   se ejecuta cada vez que se inicia una shell, por lo que cualquier instrucción en él afecta directamente el comportamiento del login.

### Solución 
Aunque no podemos iniciar sesión de forma interactiva. SSH permite ejecutar comandos remotos directamente sin necesidad de abrir una shell.
Primero,  listamos el contenido del directorio home: 
`ssh bandit18@bandit.labs.overthewire.org -p 2220 ls  
Observamos que existe el archivo `readme`, procedemos a leer su contenido:
`ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme`
Esto nos muestra el contenido del archivo, donde se encuentra la contraseña del siguiente nivel 

Este nivel nos muestra cómo es posible evadir restricciones de inicio de sesión interactivo utilizando ejecución remota de comandos a través de SSH.

![](imgs/bandit18.png)
## 🔥Level19  - bandit19 - 🔑password: cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8
- **Objetivo:** encontrar la password para el siguiente nivel.
- **Comando utilizados:** `ls, cat, file`

### Análisis 
En este nivel podemos ejecutar un archivo `setuid`, este tiene permisos especiales en Linux, hace que un programa se ejecute con los privilegios del propietario del archivo, no con los del usuario que lo ejecuta. Esto permite ejecutar comandos con privilegios elevados y acceder a archivos restringidos para el usuario actual. Las contraseñas se encuentran en la ruta `/etc/bandit_pass`
### Solución 
Listamos los archivos del directorio con el comando 
`ls -la`
Esto nos permite listar todos los archivos y ver sus permisos, nos encontramos el archivo `bandit20-do` con permisos -rwsr-x--- (la **s** nos indica que es un bit especial SUID), el cual nos va a permitir ejecutarlo con los permisos del propietario **bandit20**, no como **bandit19**.
Este archivo binario `bandit20-do` permite ejecutar comandos como el usuario bandit20, actuando así parecido al comando `sudo`
A continuación procedemos a ejecutar el archivo y a listar el contenido de los archivos de la ruta que nos han dado como pista
`./bandit20-do ls /etc/bandit_pass/`
podemos ver que tenemos un archivo con nombre bandit20, así que procedemos a ver su contenido
`./bandit20-do cat /etc/bandit_pass/bandit20`
como salida tenemos la contraseña y resuelto el nivel.

Este tipo de configuraciones puede ser crítico en entornos reales, ya que un binario SUID mal configurado puede permitir escaladas de privilegios.
![](imgs/bandit19.png)

## 🔥Level20  - bandit20 - 🔑password: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
- **Objetivo:** encontrar la contraseña para el siguiente nivel.
- **Comandos utilizados:** `nc, echo, ls,`

### Análisis
Se identifica archivo binario setuid en el directorio home (`suconnect`).
Este binario actúa como cliente: se conecta a un puerto en localhost que podemos especificar y enviamos la contraseña de bandit20.
El usuario debe actuar como servidor para responder a la conexión.

### Solución 
Primero listamos los archivos del directorio 
`ls -la`
como salida tenemos un archivo con nombre `suconnect` y con permisos -rwsr-x---, lo cual nos indica que es un archivo binario setuid
Se abre un servidor en localhost que espera la conexión del binario.
El binario se conecta al servidor y envía la contraseña de bandit20 automáticamente. 
`echo "0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO" | nc -l 12345`
- `echo` envía  la contraseña .
- `|`envía la salida al siguiente comando
- `nc`netcat: es una herramienta para conexiones de red 
- `-l 12345` el puerto de escucha 
![](imgs/bandit20.png)

Luego ejecutamos el archivo setuid en el mismo puerto.
`./suconnect 12345`
De esta manera, el binario valida la respuesta y devuelve la  contraseña para el siguiente nivel.
![](imgs/bandit20pass.png)


## 🔥Level21  - bandit21 - 🔑password: EeoULMCra2q0dSkYj561DX7s1CpBuOBt
- **Objetivo:** encontrar la contraseña para el siguiente nivel.
- **Comandos utilizados:** `cat, ls`
### Análisis
Hay un programa que esta ejecutando automáticamente desde cron, se debe ver  la ruta:  `/etc/cron.d/`, donde se encuentran las tareas programadas.
Se debe seguir la cadena de ejecución del cron hasta encontrar dónde se filtra la información.
### Solución 
Se listan los cronjobs del sistema:
`ls -la /etc/cron.d/`
Se pueden ver los archivos y sus permisos,  se identifica el archivo  `cronjob_bandit22` con permisos -rw-r--r--, este archivo es legible por el usuario actual.
Se inspecciona su contenido:
`cat /etc/cron.d/cronjob_bandit22`
Este archivo muestra que ejecuta un script del sistema.
Se revisa el script ejecutado con cron.
El script realiza lo siguiente:
- Lee la contraseña de `/etc/bandit_pass/bandit22`
- La escribe en un archivo dentro de `/tmp`
Se accede al archivo generado
`cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv`
Se obtiene la contraseña para el siguiente nivel
![](imgs/bandit21.png)
Una configuración insegura de cron puede provocar la exposición de credenciales cuando los scripts ejecutados por usuarios privilegiados escriben datos sensibles en ubicaciones accesibles como `/tmp`, permitiendo su lectura por otros usuarios. 

## 🔥Level22  - bandit22 - 🔑password: tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q
- **Objetivo:** encontrar la contraseña para el siguiente nivel
- **Comandos utilizados:** `ls, cat`

### Análisis
Este nivel es similar al anterior. Hay un programa que se ejecuta automáticamente mediante cron, por lo que se debe revisar la ruta `/etc/cron.d`para identificar los comandos que se están ejecutando. 
### Solución
Se lista el contenido de la ruta:
`ls -la /etc/cron.d`
Entre los archivos encontramos, aparece `cronjob_bandit23`, que es el que nos interesa por su nombre. 
Se ve visualiza el contenido 
`cat /etc/cron.d/cronjob_bandit23`
![](imgs/bandit22_cronjob.png)

Observamos que se ejecuta un script con nombre `cronjob_bandit23.sh`
Se procede a ver el contenido del script
`cat /usr/bin/cronjob_bandit23.sh`
En el contenido del script, encontramos algunas variables:
-  `myname` que contiene `whoami`
-  `mytarget`que contiene `echo I am user $myname | md5sum | cut -d ' ' -f 1`, 
Se reemplaza el valor de `myname`por `bandit23` para calcular manualmente el nombre del archivo donde se almacena la contraseña.
`echo I am user bandit23 | md5sum | cut -d ' ' -f 1`,
El resultado obtenido indica un cambio en el nombre del archivo en `/tmp`donde se almacena la contraseña.
Finalmente, se visualiza el contenido del archivo:
`cat /tmp/8ca319486bfbbc3663ea0fbe81326349`
De esta manera obtenemos la contraseña para el siguiente nivel.
![](imgs/bandit22_pass.png)

##  🔥Level23  - bandit23 - 🔑password: 0Zf11ioIjMVN551jX3CmStKLYqjk54Ga
- **Objetivo:** encontrar la contraseña para el siguiente nivel.
- **Comandos utilizados:** `ls, cat, mktemp, touch, nano, chmod, cp`

### Análisis
Este niveles es similar  a los dos anteriores, ya que existe un proceso automático ejecutado mediante `cron`
El primer paso consiste en revisar la ruta 
`ls -la /etc/cron.d`
Entre los archivos se observa:
`cronjob_bandit24`
Se procede a visualizar su contenido:
`cat /etc/cron.d/cronjob_bandit24`
El archivo indica que se ejecuta el siguiente script:
`cat /usr/bin/cronjob_bandit24.sh
Al analizar el script se observa que utiliza la variable
`myname=$(whoami)`
Posteriormente, el script ejecuta automáticamente cualquier archivo ubicado en:
`/var/spool/bandit24/foo`
Se requiere crear un script  para obtener la contraseña de `bandit24` y la copie a un archivo el cual sea accesible desde nuestro usuario.

### Solución

Se procede a crear un directorio temporal para trabajar:
`mktemp -d`
Dentro del directorio temporal, se crea un archivo donde se almacenará la contraseña
`touch password`
A continuación se  crea el script:
`nano bandit24_password.sh`
Contenido del script
`#!/bin/bash ` 
`cat /etc/bandit_pass/bandit24  > /tmp/.../password` 
Este script permite leer la contraseña y la dirige  al archivo `password`.
Se dan permisos de ejecución  al script
`chamod 755 bandit24_password.sh`
También se otorgan permisos al directorio temporar para permitir que el cronjob escriba en el
`chmod 777 /tmp/tmp.eJYrF6GkQY`
De igual manera se dan permisos al archivo.
`chmod 777 password`
![](imgs/bandit23_script.png)
Finalmente se copia  el script a la ruta obtenida  en el `cronjob`. 
`cp bandit24_password.sh /var/spool/bandit24/foo/bandit24_password.sh`
Después de aproximadamente un minuto, el cronjob ejecutará el script automáticamente.
Se verifica el contenido del archivo
`cat password`
Obteniendo la contraseña para el siguiente nivel. 
![](imgs/bandit23_pass.png)
## 🔥Level24  - bandit24 - 🔑password: gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8
- **Objetivo:** encontrar la contraseña para el siguiente nivel.
- **Comandos utilizados:**

### Análisis
Este nivel se indica que la contraseña se encuentra en un archivo demonio en el puerto 30002, el cual pide un código de cuatro dígitos, para poder dar la contraseña.

### Solución
Se debe crear un script para obtener la contraseña
se crea un directorio temporal 
`mktemp -d`
Luego se crea el script
`nano force_brute.sh`
Contenido del script
`#!/bin/bash
`for num in $(seq -w 0000 9999)
`do
    `echo gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $num >> possible_password.txt`
`done`
`cat possible_password.txt | nc localhost 30002 > result.txt`
![](imgs/bandit24_script.png)
Se otorgan permisos de ejecución al script
`chmod +x force_brute.sh`
A continuación se ejecuta el script
`./force_brute`
Se listan los archivos 
`ls`
Como salida, los dos archivos creados en el script
`possible_password.txt y result.txt`
Se ordena y verifica el resultado
`sort result.txt | grep -v "Wrong"`
- sort ordena el contenido del archivo
- grep -v "Wrong": omite todo el contenido que comience o contenga esa palabra
De esta manera tenemos como resultado la contraseña para el siguiente nivel.
![](imgs/bandit24.png)


## 🔥Level25  - bandit25 - 🔑password: iCi86ttT4KSNe1armKiwbQNmB3YJP3q4
- **Objetivo:** encontrar la contraseña para el siguiente nivel.
- **Comandos utilizados:**

### Análisis
En este nivel se nos indica que para obtener la contraseña para el siguiente nivel es sencillo, pero la **shell** del usuario bandit26 no es `/bin/bash`
Se procede a verificar el contenido en la ruta y los permisos de la contraseña de bandit26
`cat /etc/passwd | grep bandit26`
`ls -la /usr/bin/showtext`
A continuacion se compruega el contenido del archivo
`cat /usr/bin/showtext`
como salida se observa `#!/bin/sh`que es la shell que esta utilizando.
Tenemos información de la shell, se procede a listar los archivos
`ls `
Se observa una clave privada, la cual permitira la conexion por ssh al nivel bandit26
![](imgs/bandit25_ls.png)

### Solución
Se debe dar permisos a la clave privada para que el usuario propietario pueda leer, modificar y ejecutar. 
Dentro del laboratorio se observa que no tenemos permisos para cambiar los permisos de la clave privada.
Se procede a copiar la clave privada y a crear un archivo en la maquina local , pegar la clave y darle permisos
`nano bandit26.sshkey`
`chmod 700 bandit26.sshkey`

![](imgs/bandit25_key-1.png)
A continuación nos conectamos por `ssh`con la clave privada
	`ssh -i bandit26.sshkey bandit26@bandit.labs.overthewire.org -p 2220`
Se observa que se  inicia sesión, pero la conexón se cierra porque ejecuta `/usr/bin/showtext`y esta ejecuta una **shell** `!/bin/sh`, anteriormente al verificar el contenido de este, el script llamado `showtext`abre un archivo con nombre `text.txt `con el programa `more`.
![](imgs/bandit25_conection-1.png)
![](imgs/bandit25_conectionclose-1.png)
Para evitar que se cierre la conexión se debe poner la terminal mas pequeña, de esta manera podemos ver el comando `more`, este nos permitirá usar `vim`, de esta manera podemos interactuar.
Cuando se observa `more`, se presiona `v`para entrar en vim.
![](imgs/bandit25_more.png)
Se  ejecuta: 
- `:e /etc/bandit_pass/bandit26`para obtener la contraseña directamente
![](imgs/bandit25_e.png)
- `:set shell=/bin/bash`para modificar la shell y asi poder interactuar. 
![](imgs/bandit25_set.png)
Finalmente `:shell`, de esta manera se tiene una shell interactiva .
Se procede a buscar la contraseña para el siguiente nivel.
`cat /etc/bandit_pass/bandit26`
![](imgs/bandit25_pass.png)
## 🔥Level26  - bandit26 - 🔑password: s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ
- **Objetivo:** encontrar la contraseña para el siguiente nivel.
- **Comandos utilizados:** `ssh, ls, cat, vim`

### Análisis
Al ingresar al nivel, se obtiene conexión con el servidor ssh pero se cierra la misma inmediatamente, igual que sucedió con el nivel anterior. 
Se observa que, tras autenticarse, no se inicia una shell interactiva convencional. En su lugar, se finaliza la sesión inmediatamente 
### Solución
Se procede a reducir el tamaño de la terminal, luego ingresamos al servidor por ssh
`ssh bandit26@bandit.labs.overthewire.org -p 2220`
Al reducir el tamaño antes de la conexión, el contenido mostrado por el  programa `more` no puede visualizarse completamente, esto permite interactuar con el y utilizar la tecla `v` para abrir el editor **vim**.
Ya con esto, podemos hacer la terminal mas grande para trabajar mejor.
Se ejecuta el comando para cambiar de **shell** y poder interactuar
`:set shell=/bin/bash`
`:shell`
Con la shell interactiva, se procede a listar el contenido de los archivos y sus permisos
`ls -la`
Como salida hay dos archivos, 
- `bandit27-do`
- `text.txt`
El archivo `bandit27-do`posee el bit `SUID` activado. Esto signicfica que, al ejecutarlo, el proceso se ejecutará  con los privilegios del dueño del archivo en lugar de los del usuario actual.
Se procede a ejecutar el archivo y buscar la contraseña del nivel bandit27.
`./bandit27-do cat /etc/bandit_pass/bandit27`
De esta manera se obtiene la contraseña para el siguiente nivel.
![](imgs/bandit26_pass.png)
## 🔥Level27  - bandit27 - 🔑password: upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB
- **Objetivo:** encontrar la contraseña para el siguiente nivel.
- **Comandos utilizados:** `git, ls, cat, cd, ssh`
### Análisis
Para encontrar la contraseña del siguiente nivel, se indica que debemos descargar un repositorio en git a la maquina local, este nos pedirá contraseña al momento de ingresar por ssh al repositorio, la cual es la misma que se uso para ingresar a  `bandit27`
### Solución
Se clona el repositorio de git 
`git clone ssh://bandit27-git@bandit.labs.overthewire.org:2220/home/bandit27-git/repo`
Se ingresa la contraseña , se descarga el repositorio.
![](imgs/bandit27_conecction.png)
Se listan los archivos
`ls`
Como salida tenemos un directorio con nombre`repo`
Se accede a este y se listan los archivos nuevamente
`cd repo`
`ls`
![](imgs/bandit27_conecction.png)
Se obtiene un archivo con nombre `README`
Se procede a ver su contenido
`cat README`
Como resultado se obtiene la contraseña para el siguiente nivel
![](imgs/bandit27_pass.png)

## 🔥Level28  - bandit28 - 🔑password: Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN
- **Objetivo:** encontrar la contraseña para el siguiente nivel.
- **Comandos utilizados:** `ls, cd, cat, git clone, git log, git show`

### Análisis
Nos encontramos en la misma situación del nivel anterior, donde se nos indica que para obtener la contraseña para el siguiente nivel, se debe clonar un repositorio en nuestra máquina local,  la contraseña para clonar el repositorio es la misma del nivel actual. 

### Solución 
Se  clona el repositorio por git
`git clone ssh://bandit28-git@bandit.labs.overthewire:2220/home/bandit28-git/repo`
A continuación se introduce la contraseña de este nivel, la cual permitira la descarga del repositorio
Se listan los archivos
`ls `
Como salida se obtiene el directorio con nombre `repo`
Se accede a este
`cd repo`
Se listan los archivos y se observa el archivo `README.md`, con extensión `.md`(Markdown).
Se verifica su contenido 
`cat README.md`
No se observa información relevante.  
![](imgs/bandit28_ls.png)
Se procede a verificar el historial de cambios del archivo con
`git log`
Al revisar el historial de commits, se identifica un commit anterior que contenía una versión diferente del archivo `README.md`
![](imgs/bandit28_gitlog.png)
Para analizar las modificaciones introducidas en dicho commit, se ejecuta:
`git show commit adc7f885a129baee883058b8a870739489f80194`
Esto permite examinar el contenido exacto de la modificación.
Se muestra en el `diff`del commit información relevante, incluida la contraseña para el siguiente nivel. 
![](imgs/bandit28_gitshow.png)
Tras verificar cambios en el historial del repositorio y analizar el contenido del commit anterior, se recupera la información eliminada del archivo `README.md`, obteniendo la contraseña necesaria para el siguiente nivel. 


## 🔥Level29  - bandit29 - 🔑password: 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7
- **Objetivo:** encontrar la contraseña para el siguiente nivel.
- **Comandos utilizados:** `ls, git clone, cd, git branch, git show, git switch, cat`

### Análisis 
Este nivel, es similar a los dos anteriores, se debe clonar un repositorio git en nuestra máquina local, luego verificar su contenido para encontrar la contraseña del siguiente nivel. 

### Solución 
Se clona el repositorio en nuestra maquina local 
`git clone ssh://bandit29-git@bandit.labs.overthewire.org:2220/home/bandit29-git/repo`
A continuación se introduce la contraseña de este nivel, la cual permitira la descarga del repositorio
![](imgs/bandit29_gitclone.png)
A continuación se verifican los archivos
`ls`
Como resultado se observa un directorio con nombre `repo`
Se accede al directorio
`cd repo `
El resultado muestra un archivo con nombre `README.md` con extensión `.md` (Markdown).
Posteriormente se verifica su contenido
`cat README.md`
Sin resultados relevantes en la salida. 
![](imgs/bandit29_ls.png)
Se verifica el historial del git 
`git log`
Al verificar el historial se observa que hay modificación en uno de los commits
Se inspecciona la modificación del commit
`git show 921cad124cfe5b4ba9f648de1894f75656ff0ff4` 
![](imgs/bandit29_gitlogshow.png)
 Se observa que han habido cambios en el commit, sin poder ver la contraseña.
 Se procede a verificar las ramas con el comando 
 `git branch -a`
 Como salida se observa diferentes ramas, hay que verificar  cada una, entre ellas nos quedamos con  la rama con nombre `dev`
 `git switch dev`
 ![](imgs/bandit29_gitbranch.png)
 Luego de cambiar de rama, nuevamente se verifica el historial
 `git log`
 Posteriormente verificar el commit
 `git show 97622e03dcbefc7953e906cecbc8a602f84cba4a`
 ![](imgs/bandit29_gitshowdev.png)
Al observar  el historial del commit en la rama con nombre`dev`, se observa su contenido. Obteniendo la contraseña para el siguiente nivel 
 
## 🔥Level30 - bandit30 - 🔑password: qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL
- **Objetivo:** encontrar la contraseña para el siguiente nivel.
- **Comandos utilizados:**

### Análisis
Para obtener la contraseña del siguiente nivel se debe clonar un repositorio git en nuestra maquina local, similar a los niveles anteriores. 

### Solcución
Se clona el repositorio Git
`git clone ssh://bandit30-git@bandit.labs.overthewire.org:2220/home/bandit30-git/repo' 
A continuación se introduce la contraseña de este nivel, la cual permitirá la descarga del repositorio
Se listan los archivos
`ls`
Como salida un directorio con nombre `repo`
Se accede al directorio
`cd repo`
De igual manera se listan  los archivos
`ls`
El comando devuelve un archivo con nombre `README.md`
Se procede a ver su contenido
`cat README.md`
![](imgs/bandit30_ls.png)
No se observa información importante
A continuación se verifica el historial del git
`git log`
Como salida se observa el commit
Se procede a verificar el commit
`git show bd393e0e59a075f92fd84edc0ad8d13f64572de2`
Este no muestra información importante
Posteriormente se verifican las ramas
`git branch -a`
Como salida tampoco se obtiene información relevante
![](imgs/bandit30_log.png)
Al verificar los commits y las ramas no se obtiene información relevante, se revisan las etiquetas del repositorio, en Git se pueden almacenar referencias importantes mediante tag
`git tag`
El resultado muestra una etiqueta con nombre `secret`
Se verifica el contenido
`git show secret`
![](imgs/bandit30_pass.png)
Este comando nos muestra el contenido de la etiqueta, la cual revela la contraseña del siguiente nivel.




## 🔥Level31 - bandit31 - 🔑password: fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy
- **Objetivo:** encontrar la contraseña para el siguiente nivel.
- **Comandos utilizados:**

### Análisis
Para obtener la contraseña del siguiente nivel se debe clonar un repositorio Git en la maquina local, luego interpretar las instrucciones contenidas en el archivo `README` y realizar los cambios solicitados para posteriormente enviarlos al repositorio remoto. 

### Solución
Se clona el repositorio git en la maquina local
`git clone ssh://bandit31-git@bandit.labs.overthewire.org:2220/home/bandit31-git/repo`
Este pide una contraseña, la cual es la del nivel actual
Se ingresa la contraseña y se procede a verificar el contenido de los archivos
`ls `
Como salida un directorio con nombre `repo`
Se accede al directorio clonado
` cd repo`
A continuación se verifica su contenido 
`ls`
Se encuentra un archivo con nombre `README`
![](imgs/bandit31ls.png)
Al verificar su contenido con 
`cat README`
Este indica que se debe subir un archivo al repositorio, con algunos criterios
- nombre: `key.txt`
- contenido: `May I come in`
- branch: `master`
Basándose en en la información se procede a crear el archivo `key.txt`
`echo "May I come in" > key.txt`
A continuación se procede a enviar el archivo al repositorio 
`git add -f key.txt`
Debido a que el repositorio continee un archivo `.gitignore` que excluye todos los archivos con extensión `.txt`. Git ignora `key.txt`de forma predeterminada. 
La opción `-f` (force) permite agregarlo al área de preparación (staging área) ignorando dicha restricción
Alternativamente, podría modificarse el archivo `.gitignore` para excluir únicamente aquellos archivos que se desean rastrear. Sin embargo, para este ejercicio resulta mas sencillo utilizar `git add -f`, que fuerza la inclusión del archivo ignorado. 
Se verifica el estado el estado del repositorio
`git status`
Luego de haber añadido el archivo al repositorio, se procede a confirmar los cambios 
`git commit -a`
![](imgs/bandit31_gitadd.png)
Git informó que la rama local `master` estaba adelantada respecto a `origin/master` por un commit. Esto indica que existe al menos un commit almacenado localmente que todavía no ha sido enviado al repositorio remoto. 
Para publicar dichos cambios y sincronizar ambas ramas se debe ejecutar 
`git push -u origin master`.
La opcion `-u`establece una relación de seguimiento (upstream) entre la rama local y la remota, permitiendo utilizar posteriormente `git push` sin especificar la rama. 
![](imgs/bandit31_pass.png)
Este pedirá la contraseña del nivel, luego de introducirla se mostrara la contraseña para el siguiente nivel. 
## 🔥Level32 - bandit31 - 🔑password: 3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K 
- **Objetivo:** encontrar la contraseña para el siguiente nivel.
- **Comandos utilizados:**


