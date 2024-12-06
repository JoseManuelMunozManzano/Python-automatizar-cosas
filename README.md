# PYTHON - AUTOMATIZACIÓN DE TAREAS

Desde Day_01 a Day_20 se enseña lo básico de Python, apoyado por la creación de una app de tareas que se hace tanto como app de consola, escritorio y web app.

Luego comenzamos con la automatización, ya no con nombre Day_xx sino con el nombre que indica el tipo de automatización a realizar.

## Day_01

- 01-Build-Todo-List-App
    - Una lista de todos en consola
    - main.py
- 02-Bonus
    - Programa que comprueba el título de un libro y nos da la longitud de ese título
    - main.py
- NOTAS:
    - Para abrir la consola de Python en VSCode, en un fuente de Python, sobre una línea de Python, pulsar: `Shift+Enter`
    - Otra forma que sirve en general: Pulsar `Ctrl+Shift+P` y escribir `Python: Start Terminal REPL`
    - Otra forma consiste en, una terminal de Linux, escribir: `python`, y aparecerá la consola de Python
    - Salir de la consola con `quit()`
    - En este día aprendemos: variables, listas, strings, funciones `print()`, `input()`, `type()` y `len()`
    - Las funciones se aplican directamente, sin notación de punto
    - Con la función `exit()` termina el programa

## Day_02

- 01-Build-Todo-List-App
    - Seguimos con este programa
    - main.py
- 02-Bonus
    - Dos ejemplos más del bucle while
    - bonus1.py
    - bonus2.py
- 03-Excercises
    - Distintos ejercicios para asentar lo aprendido hasta ahora
    - ex1.py
    - ex2.py
- NOTAS:
    - En este día aprendemos: bucle `while`, indentación, booleanos (True, False)
    - Método/atributo `list.append(string)`
    - Métodos/atributos `string.capitalize()`, `string.title()` y `string.upper()`
    - Los métodos se aplican a variables, con notación de punto
    - Para explorar los métodos que existen para un tipo de dato, o hacer testing, es bueno usar la consola
        - En la consola, escribir: `dir(str)` o `dir("cualquier_string")`
        - Aparecerá una lista con todos los métodos disponibles para el tipo de dato string, ordenados alfabéticamente
        - Con la función help(), se puede obtener ayuda de un método concreto. Escribir: `help(str.upper)` o `help("cualquier_string".upper)`
        - Pulsar la tecla `q` para salir de la ayuda
    - Para obtener una lista de funciones que se pueden aplicar, usar la consola
        - En la consola, escribir: `import builtins`, pulsar Intro y escribir `dir(builtins)`
        - Aparecerá una lista con todas las funciones disponibles, ordenadas alfabéticamente
    - Se puede hacer lo mismo desde un programa Python, pero siempre usando la función print, por ejemplo: `print(dir(str))`

## Day_03

- 01-Build-Todo-List-App
    - Seguimos con este programa
    - main.py
- 02-Bonus
    - Un ejemplo con el bucle for
    - bonus.py
- NOTAS:
    - En este día aprendemos cómo hacer que un programa tome decisiones usando `match ... case`
        - Para cualquier valor no definido en los case, en Python se usa, por convención `case _:`
    - Salir de un bucle usando `break`
    - Operador OR: `|`
    - Bucle `for ... in`
    - Eliminar espacios en blanco de una cadena usando el método `variable.strip()`
        - No cambia el valor del string, sino que devuelve una nueva cadena sin esos espacios en blanco
        - Si se indica valor como argumento, lo elimina del principio y del final

## Day_04

- 01-Build-Todo-List-App
    - Seguimos con este programa, añadiendo la posibilidad de editar una tarea
    - main.py
- 02-Bonus
    - Vamos a aprender sobre la mutabilidad en Python y las tuplas
    - main.py
- NOTAS:
    - En este día aprendemos como acceder a una lista usando un índice `todos[0]`
    - Función que convierte de str a int: `int('10')`
    - Función que convierte de str a float: `float('10.12')`
    - Función que convierte de int a str: `str(10)`
    - Obtener el índice de un elemento de una lista usando su valor: `mylist.index('b')`
    - Los métodos que comienzan y terminan con doble guión bajo, se pueden usar, pero existen para que Python los use internamente
        - Ejemplo: `mylist.__setitem__(1, 'd')` es lo mismo que `mylist[1] = 'd'`, siendo este último el que debemos usar
    - Las listas son mutables
    - Las tuplas son la versión inmutable de una lista
    - Los str son inmutables. Para modificar uno, necesitamos usar el método `mystring = mystring.replace('.', '-', 1)`
        - Pero esto no modifica el str original, sino que devuelve un nuevo str, de ahí la asignación
        - El 1 indica la cantidad de ocurrencias que queremos reemplazar

## Day_05

- 01-Build-Todo-List-App
    - Seguimos con este programa, añadiendo el número de la tarea cuando se indica la opción show (o sh)
    - También permitimos que el usuario marque una tarea como completada, borrándose de la lista de tareas por hacer
    - main.py
- 02-Bonus
    - Vamos a repasar uso de listas y de f-strings, y vamos a ordenar elementos de una lista alfabéticamente
    - main.py
- NOTAS:
    - En este día aprendemos la función `enumerate(mylist)`
        - Con esta función obtenemos el índice y el valor de un elemento de una lista (o de un str)
        - La función devuelve un `enumerate object`
        - Para obtener una representación de ese objeto en la consola de Python, usar la función list: `list(enumerate(mylist))`
        - Vemos que enumerate devuelve una lista de tuplas
        - Con enumerate, podemos indicar el número por el que empieza el índice, 1 en este ejemplo: `enumarate(mylist, 1)`
    - Uso de `f-strings`, donde, dentro de unas llaves, se pueden indicar variables
        - Se forman de la siguiente manera: `f"{var_1} {var_2}"`
    - Eliminar elementos de una lista usando el método `mylist.remove(value)`
    - Eliminar todos los elementos de una lista usando el método `mylist.clear()`
    - Eliminar y devolver un elemento de una lista, por defecto el último, con el método `mylist.pop(index)`
        - El índice 0 es el primero de la lista, el 1 el segundo, el -1 es el último de la lista, el -2 el penúltimo...
    - Ordenar una lista en forma ascendente usando el método `mylist.sort()` y en forma descendente usando el método `mylist.sort(reverse=True)`
    - Otra forma de ordenar que también vale para tuplas y que sí devuelve una nueva lista/tupla/str consiste en usar la función `sorted(mytuple)`

## Day_06

- 01-Build-Todo-List-App
    - Seguimos con este programa, donde vamos a almacenar los items de tareas en ficheros de texto
    - El archivo de texto se encuentra en el directorio raiz, en `data/todo_list/todos.txt`
    - main.py
- 02-Bonus
    - Vamos a trabajar con archivos de texto y usar la función zip()
    - main.py
- 03-Excercises
    - Ejercicios para practicar con ficheros de texto
    - ex1.py
    - ex2.py
    - ex3.py
- NOTAS:
    - En este día aprendemos a trabajar con ficheros de texto para almacenar/recuperar información
    - Se usa la función `file=open('path/file.txt', 'w')` para devolver un tipo de objeto `<class '_io.TextIOWrapper'>`
        - Si encuentra el archivo, lo borra y lo crea de nuevo
        - Lo que hay que hacer para no perder los elementos es escribirlos antes en una lista
        - El segundo argumento hace mención a la forma de usar el archivo, en este caso w=write
        - Usar help(open) para ver todas las posibilidades que ofrece esta función
        - Para escribir en el fichero todos los elementos de una lista, usar el método `file.writelines(mylist)`
        - Para escribir una sola línea de string, se puede usar el método `file.write("my text\n")`
        - Para escribir en una lista cada una de las líneas de un fichero, usar el método `file.readlines()`
            - Abrir el fichero en modo lectura, usando r=read
        - Con el método `file.read()` obtenemos todo el contenido del fichero como un string
            - Tener en cuenta que al leer, se usa un cursor interno. Cuando se lee, el cursor se mueve, así hasta el final
            - Una vez leído un fichero no se puede volver a leer sin cerrarlo primero y volver a abrirlo en modo lectura (con 'r')
        - Para cerrar un archivo, se usa el método `file.close()`
    - Importar, usando `import`
    - Obtener el path actual del archvo .py que se está ejecutando `os.path.dirname(__file__)`
    - Unir rutas al path, usando `os.path.join(os.path.dirname(__file__), 'path/file.txt')`
    - Documentación: https://es.stackoverflow.com/questions/593072/qu%C3%A9-es-el-directorio-de-trabajo-actual-c%C3%B3mo-lo-determino-y-c%C3%B3mo-lo-cambio
    - Terminar el programa para que se escriba en el fichero
        - No hace falta si se indica `file.close()`
    - Usar raw strings para que una cadena se trate tal cual, sin intentar escapar caracteres, por ejemplo: `r"C:\Users\jm\Downloads\todos.txt"`
    - Usar la función `c = zip(a, b)`, que funciona parecido a enumerate(). Dadas dos listas, a y b, con zip vamos cogiendo un elemento de cada una de las listas
        - Ejecutando `list(c)` obtenemos una lista de tuplas, en la forma `[(value_a1, value_b1), (value_a2, value_b2)...]`
    - Dividir un string en distintas líneas, usando `\`

## Day_07

- 01-Build-Todo-List-App
    - Seguimos con este programa, donde vamos a hacerlo más amigable para el usuario
    - main.py
- 02-Bonus
    - Practicamos con list comprehensions
    - main.py
- NOTAS:
    - List comprehensions. Son equivalentes a un bucle for y sirven para modificar elementos de una lista
        - Se hacen en una sola línea y comienzan con corchetes.
        - Ejemplo: `new_todos = [item.strip('\n') for item in todos]`
        - Recordar que el método `str.strip('mystr')` elimina el texto deseado del string del principio y del final
    - La función `result = sum(mylist)` suma todos los elementos de una lista

## Day_08

- 01-Build-Todo-List-App
    - Seguimos con este programa, donde vamos a mejorar el código (refactorización) para manejar mejor los archivos
    - main.py
- 02-Bonus
    - Vamos a crear una aplicación de un diario para seguir trabajando con ficheros y con el gestor de contexto `with`
    - journal.app
- NOTAS:
    - Uso del gestor de contexto `with` para manejar ficheros de una manera más eficiente
    - Por ejemplo: `with open(path, 'r') as file:`
    - Con esto, al terminar el bloque, se gestiona de forma automática el cierre del fichero, incluso aunque el programa termine de forma abrupta

## Day_09

- 01-Build-Todo-List-App
    - Vamos a mejorar la característica add, permitiendo informar add seguido del todo, en una línea, sin necesidad de pulsar Intro
    - Eso hace que tengamos que cambiar `match .. case` por `if .. elif .. else`
    - main.py
- 02-Bonus
    - Vamos a hacer un programa que comprueba la fortaleza de una contraseña
    - El objetivo es practicar con las sentencias `if .. elif .. else` y expresiones booleanas
    - También vamos a ver un nuevo tipo de datos: Diccionarios
    - main.py
- NOTAS:
    - Operador `in` sirve para saber si un string está contenido en otro string
        - or ejemplo: `'add' in 'add Play Chess'` devuelte True o False
    - Uso de condicionales `if`, `elif` y `else`
        - Una forma de programar que una variable está entre dos valores es usar esta construcción: `if 0 < temperature < 100:`
    - Uso de substrings (o slicing). Por ejemplo, `todos = user_settings[4:]` nos devuelve la cadena a partir del índice 4 (empiezan en 0)
        - Si indicamos `todos = user_settings[4:9]` obtenemos del índice 4 al 8 inclusive, pero no el 9
    - Uso de operadores booleanos, como `or`, `and`, `not`
        - `not` se puede usar en conjunción con el operador `in` para negar. Por ejemplo: `if 'add' not in user_action`
    - Para comprobar si un string es un número se usa el método `"123".isdigit()`
    - Para comprobar si un string está en mayúsuclas se usa el método  `"HELLO".isupper()`
    - Para devolver True cuando todos los elementos de una lista son True, o False en caso contrario, usar `all(mylist)`
    - Vemos también diccionarios, un nuevo tipo de dato que usa llaves y cuyos valores se componen de un par clave-valor separados por los dos puntos. Cada elemento se separa del siguiente por una coma
        - Ejemplo: `a = {"height": 14, "width": 20, "depth": 30}`
        - El tipo de dato es `dict`
        - Es un tipo de dato muy útil cuando queremos saber qué significa cada value (la key se conoce como la metadata), como en el ejemplo dado
        - Para acceder a un elemento de un diccionario se usa su key: `a["width"]`
        - Para añadir datos a un diccionario se indica la clave y su valor: `a["area"] = 100`
        - Para acceder a los valores de un diccionario, usamos el método `a.values()`
            - Se obtiene como un tipo de lista, cuyo tipo se llama objeto `dict_value`
        - Para acceder a las keys de un diccionario usamos el método `a.keys()`
            - Se obtiene como un tipo de lista, cuyo tipo se llama objeto `dict_keys`
        - Para usar el método `all()` con diccionarios, mirando sus valores, usaremos `all(a.values())`

## Day_10

- 01-Build-Todo-List-App
    - Se corrige un error del programa por el cual, si se informa edit seguido de add, lo que hace es añadir un nuevo todo porque entra por el add
    - Se sustituye el operador `in` por el método `str.startswith('string')`
    - Se realiza gestión de errores
    - main.py
- 02-Bonus
    - Ejemplo con try .. except y tratar errores de lógica usando if
    - main.py
- NOTAS:
    - Vemos el método `str.startswith('string')` para saber si una cadena de texto comienza por un texto concreto
    - Vemos manejo de errores con el bloque `try .. except .. finally`
    - Vemos la sentencia `continue`
    - Función `exit("string")` para terminar un programa
        - También se puede usar `exit()`, sin string

## Day_11

- 01-Build-Todo-List-App
    - Mejoramos nuestro programa usando funciones personalizadas, eliminando redundancia en nuestro código
    - main.py
- 02-Bonus
    - Creamos una función que obtiene números de un archivo de texto y devuelve la media de esos números
    - main.py
- NOTAS:
    - Aprendemos a crear nuestras propias funciones personalizadas
        - Se usa la palabra reservada `def nombre_funcion():`
        - Para separar una función de otras partes del código, se recomienda dejar dos líneas de separación
        - Intentar que el nombre de una variable local no exista también como nombre de variable global
        - Se usa `return myvalue` para indicar que se devuelve algo
        - Si una función no devuelve nada, pero la llamada se asigna a una variable, entonces el valor devuelto es `None`
        - Es equivalente indicar `return None`
    - La función `max(mylist)` devuelve el valor máximo de una lista
    - La función `min(mylist)` devuelve el valor mínimo de una lista
    - Para utilizar la función matemática de potencia, se usa `**`, por ejemplo: `2 ** 5` indica 2 elevado a 5

## Day_12

- 01-Build-Todo-List-App
    - Seguimos trabajando con funciones personalizadas, esta vez, aceptando argumentos en su llamada
    - main.py
- 02-Bonus
    - Seguimos explorando el uso de funciones, donde vemos el concepto de desacoplamiento del resultado
    - main.py
- NOTAS:
    - Nuestras funciones personalizadas, ahora aceptan argumentos de entrada
        - Terminología: la función se define con `parámetros`, pero, al llamar a dicha función, se llama con `argumentos`
        - Se puede indicar, opcionalmente, el nombre del argumento en la llamada a la función: `get_todos(filepath="todos.txt")`
    - Uso del método `split` para separar cadenas por el string indicado. Su resultado se asigna a una lista
        - Ejemplo: `mylist = mystring.split(" ")`

## Day_13

- 01-Build-Todo-List-App
    - A los parámetros de nuestras funciones personalizadas se les asigna valores por defecto
    - También aprendemos a crear docstrings
    - main.py
- 02-Bonus
    - Seguimos viendo el tema de desacoplamiento que vimos en Day_12
    - main.py
    - converters.py
- NOTAS:
    - Se pueden asignar valores por defecto a los parámetros de una función
        - Ejemplo: `def get_todos(filepath="todos.txt"):`
        - Ahora, al realizar la llamada, no hace falta indicar ningún argumento, y cogerá el valor por defecto: `todos = get_todos()`
        - Los parámetros que tienen un valor por defecto deben aparecer al final de la lista de parámetros de la función: `def write_todos(todos, filepath="todos.txt"):`
    - Crear `docstring` para documentar el código
        - Se recomienda crear esta documentación para cada función de nuestro programa
        - Se escriben en la primera línea tras la definición de la función
        - Se usan triples comillas, `""" My documentation """`
        - Si hay más de una línea, el texto se alinea debajo de la primera comilla:
        - ```
            """
            Si hay más de una línea de texto de documentación.

            Se alinéan debajo de la primera comilla.
            """
          ```
        - En el programa podemos ejecutar, como prueba, la función `print(help(get_todos))` y veremos el docstring creado
    - El uso de las triples comillas también se usa en Python para informar varias líneas de texto
        - Si imprimimos la variable que tiene asignada ese texto, veremos que aparece tal cual se ha informado, sin necesidad de `\n` para cambiar de línea
        - Para tener múltiples líneas usando comillas, necesitamos, al final de cada línea, escribir `\`
    - Extraer una tuple a sus variables: `feet, inches = (5, 12)`

## Day_14

- 01-Build-Todo-List-App
    - Continuamos este programa, organizando el código en módulos, separando las funciones en un archivo separado
    - main.py
    - functions.py
- 02_Bonus
    - Seguimos viendo el tema de desacoplamiento que vimos en Day_12 y Day_13
    - Hemos cambiado el return, de tuplas a diccionarios, como práctica
    - Queremos separar la funcionalidad del programa en diferentes módulos que importaremos al programa principal
    - main.py
    - converters.py
    - parsers.py
- NOTAS:
    - Importar módulos desde el "backend" al "frontend"
    - Importar módulos usando la siguiente sintaxis: `from my_module import function1, function2` separando las funciones que se quieren importar con comas
        - Esto funciona siempre que main.py y my_module.py estén en el mismo directorio
        - Si estuviera en un directorio de la carpeta del main, sería: `from folder.my_module import function1`
        - Se puede usar la función directamente en el código: `function1()`
        - Para saber las funciones disponibles, desde la consola de Python se puede ejecutar `import functions` seguido de `dir(functions)`
    - También se puede importar módulos con la sintaxis: `import my_module`
        - Esto funciona siempre que main.py y my_module.py estén en el mismo directorio
        - Para usar las funciones hay que indicar el módulo: `my_module.function1()`
        - Preferible cuando hay que importar muchas funciones
        - Preferible cuando queremos saber de qué módulo proviene cada función
    - Si el módulo a importar se encuentra en un directorio distinto a main.py, usar la sintaxis: `from directory import mymodule`
    - Cuando se importa un módulo al módulo main y se ejecuta el módulo main, en el momento en que Python lee la sentencia `import mymodule` se ejecuta mymodule por completo
    - Para evitar este comportamiento y solo ejecutar cierto código cuando el módulo importado se ejecuta como main, hay que escribir esta sentencia if: `if __name__ == "__main__":`
        - Esto lo querremos hacer, por ejemplo, para probar código
    - El método `str.count('.')` cuenta el número de puntos (en este ejemplo) que tiene un string

## Day_15

- 01-Build-Todo-List-App
    - Añadimos un mensaje de salida al usuario, indicando la fecha y hora actuales
    - main.py
    - functions.py
- 02-Experiments
    - Vemos cuatro módulos importantes que debemos aprender
    - glob, csv, webbrowser y shutil
    - https://docs.python.org/3/py-modindex.html
    - e1.py
        - Vemos el modulo glob
        - files/ideas.txt
        - files/projects.txt
    - e2.py
        - Vemos el módulo csv
        - files/weather.csv
    - e3.py
        - Vemos el módulo shutil (shell utilities)
    - e4.py
        - Vemos el módulo webbrowser
- 03-Bonus
    - Aprendemos a trabajar con estructuras JSON haciendo un programa de preguntas y respuestas
    - main.py
    - questions.json
- 04.Exercises
    - ex1.py
- NOTAS:
    - Aprendemos a importar módulos escritos por el equipo de desarrolladores de Python
        - https://docs.python.org/3/py-modindex.html
    - Aprendemos a añadir fechas y horas a nuestras apps
        - Importamos el módulo time: `import time`
        - En la consola de Python, podemos indicar `import time` seguido de `dir(time)` para ver todas las funciones disponibles
        - Usamos la función `strftime("%m - %Y")` y con los parámetros indicados obtenemos el mes y año actual
        - `strftime("%b %d, %Y %H:%M:%S")` obtenemos el nombre del mes actual, el día, el año y la hora actual
        - https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    - Aprendemos los siguientes cuatro módulos:
        - csv
        - glob
        - webbrowser
        - shutil
    - Aprendemos a trabajar con estructuras JSON importando el módulo correspondiente: `import json`
        - Es data hecha de listas y/o diccionarios y que se ponen en archivos externos con extensión .json
    - Uso del módulo `random` para generar números aleatorios

## Day_16

- 01-Build-Todo-List-Gui-App
    - Vamos a construir interfaces gráficas de usuario (GUI) con Python para escritorio
    - La app es la misma, la de tareas, pero ahora, en vez de ser una app de consola, será una app con interface gráfica para escritorio
    - Empezamos haciendo solo la parte de añadir tareas
    - gui.py
        - Este código fuente es nuestro frontend
    - functions.py
        - Este código fuente es nuestro backend
        - No lo usamos en el día de hoy
- 02-Bonus
    - Practicamos la creación de una interfaz gráfica para escritorio, haciendo un compresor de ficheros
    - Lo comenzamos en el día de hoy, haciendo la parte gráfica y lo terminaremos en Day_17, implementando su funcionalidad
    - main.py
- 03-Exercises
    - Seguimos practicando la creación de interfaces gráficas de usuario para escritorio
    - Creamos solo la GUI de un conversor de pies y pulgadas
    - ex1.py
    - Creamos sola la GUI del programa de preguntas y respuestas
    - ex2.py
- NOTAS:
    - Aprendemos a construir interfaces gráficas de usuario (GUI) con Python para escritorio
    - Usamos el módulo (o biblioteca) de terceros `FreeSimpleGUI`
        - https://docs.pysimplegui.com/en/latest/cookbook/original/
    - Una lista completa de bibliotecas de terceros de Python la podemos encontrar en el repositorio `https://pypi.org/`
    - Para instalar esta biblioteca de terceros, la buscamos en la web de repositorios de Python
        - Ahí aparece el comando de instalación: `pip install FreeSimpleGUI`
        - Copiar dicho comando en la terminal, teniendo en cuenta que esté referenciado el `entorno virtual Python` para no instalarlo globalmente, sino solo para ese entorno virtual
        - `pip` es una biblioteca de terceros que se usa para instalar otras bibliotecas de terceros
        - Si no funciona `pip`, probar a escribir `pip3`
    - Ver el programa `gui.py` para explicaciones de como usar esta biblioteca
    - Vemos como podemos crear sinónimos de módulos, para escribir menos
        - `import FreeSimpleGUI as sg` indica que ahora podemos usar `sg` en vez de `FreeSimpleGUI`
    - Vemos que los tipos de Python empiezan en mayúsculas. Por ejemplo: `sg.Text`
    
## Day_17

- 01-Build-Todo-List-Gui-App
    - Seguimos creando la parte de la interfaz gráfica y la funcionalidad del botón para añadir y editar tareas
    - gui.py
        - Este código fuente es nuestro frontend
    - functions.py
        - Este código fuente es nuestro backend
- 02-Bonus
    - Seguimos haciendo el compresor de ficheros
    - main.py
    - zip_creator.py
- 03-Exercises
    - Seguimos practicando la creación de interfaces gráficas de usuario para escritorio
    - Añadimos la funcionalidad al conversor de pies y pulgadas
    - ex1.py
    - converters.py
- NOTAS:
    - Vemos más widgets de la biblioteca `FreeSimpleGUI`
    - Usamos el módulo (o biblioteca) estándar `zipfile` para comprimir archivos
        - Da más flexibilidad que la biblioteca `shutil` a la hora de comprimir archivos
    - Usamos la biblioteca `pathlib` para obtener varios argumentos y fusionarlos para crear una ruta completa
        - Lo bueno es que, dado el sistema operativo, separará automáticamente con `\` o `/`
    - Al clonar un repositorio, si existe un archivo `requirements.txt`, ahí es donde vienen las dependencias de módulos de terceros
        - Para instalar esas dependencias, ir a la terminal y ejecutar: `pip install -r requirements.txt`

## Day_18

- 01-Build-Todo-List-Gui-App
    - Seguimos creando la parte de la interfaz gráfica y la funcionalidad del botón para marcar las tareas pendientes como completadas y eliminarlas de la lista
    - También se va a hacer un boón de salida del programa
    - Vamos a gestionar errores con `try .. catch`, añadir fecha/hora actuales y a cambiar el theme del programa y los tamaños de los widgets
    - Añadimos la creación del archivo `todos.txt` cuando este no existe
    - Generamos un ejecutable
    - gui.py
        - Este código fuente es nuestro frontend
    - functions.py
        - Este código fuente es nuestro backend
- 02-Experiments
    - Es el mismo proyecto de tareas, pero ahora experimentamos con botones, usando imágenes como botones
    - gui.py
        - Este código fuente es nuestro frontend
    - functions.py
        - Este código fuente es nuestro backend
    - add.png
    - complete.png
- 03-Bonus
    - Hacemos un programa que extraiga un archivo zip a un directorio de destino
    - Notar que todos los elementos se encuentran bien alineados (uso de Columns)
    - main.py
    - zip_extractor.py
    - compressed.zip
- 04-Exercises
    - Seguimos practicando la creación de interfaces gráficas de usuario para escritorio
    - Añadimos el botón de Exit al conversor de pies y pulgadas
    - ex1.py
    - converters.py
- NOTAS:
    - Aprendemos a hacer ventanas pop-up
    - Para obtener posibles themes para un programa: `https://docs.pysimplegui.com/en/latest/documentation/module/themes/`
    - Pasos para crear un programa:
        - Diseñar el frontend
            - Usar una hoja, Figma...
        - Programar el fronted
        - Programar el backend
        - Conectar el backend al frontend para terminar el programa
    - Importamos el módulo `os` para saber si un archivo existe: `os.path.exists("my_file.txt")`
        - Devuelve True si el archivo existe y False si no existe
    - Aprendemos a crear un fichero sin escribir nada, usando la sentencia `pass`
        - `pass` sirve para indicar que no queremos hacer nada, cuando la sintaxis requiere escribir alguna sentencia
    - Si por lo que sea, al abrir la terminal no aparece `(.venv)` ejecutar en la terminal el siguiente comando
        - `set-executionpolicy remotesigned -scope currentuser`
        - Cerrar la terminal y volver a abrirla. Debe verse ahora que estamos en el entorno virtual `(.venv)`
    - Aprendemos a crear un ejecutable que pueda ejecutarse en Mac, Linux y Windows
    - Para Windows
        - Debemos estar en el entorno virtual
        - Instalar el siguiente paquete de terceros: `pip install pyinstaller`, que sirve para crear ejecutables
        - Ejecutar en la terminal, en la carpeta del proyecto: `pyinstaller --onefile --windowed --clean <my_main_script>.py`
            - Indicando `--onefile` solo genera un fichero ejecutable
            - Indicando `--windowed` evitamos que se cree una línea de comando
            - Indicando `--clean` se sobreescribe el ejecutable anterior
        - El ejecutable se creará en el directorio del proyecto, en la carpeta `dist`
    - Para Mac
        - Instalar el programa `Platypus` usando brew: `brew install --cask platypus`
            - Indicar el nombre del ejecutable
            - Indicar el path absoluto del interprete de Python, el del entorno virtual
            - Seleccionar el path del programa Python que sea el punto de entrada al programa
                - En nuestro proyecto, sería `gui.py`
            - Indicar los fuentes Python que son necesarios para que se ejecute el programa
                - En nuestro proyecto, sería `functions.py`
            - Pulsar el botón `Create App`
        - Veremos al ejecutar el ejecutable creado que se abren dos ventanas
            - En la segunda ventana aparecen logs de bugs del programa
        - Una vez hemos visto que no se generan logs de errores, lo mejor es volver a crear el ejecutable sin esa segunda ventana
            - Hacer el mismo proceso de creación de ejecutable, pero esta vez, en `Interface` indicar `None`
    - Para Linux
        - Debemos estar en el entorno virtual
        - Instalar el siguiente paquete de terceros: `pip install pyinstaller`, que sirve para crear ejecutables
        - Ejecutar en la terminal, en la carpeta del proyeto: `pyinstaller --onefile --windowed --clean <my_main_script>.py`
            - En mi proyecto, hay que indicar `gui.py`
        - El ejecutable se creará en el directorio del proyecto, en la carpeta `dist`
        - Acceder con el gestor de archivos y pulsar doble click sobre el para ejecutarlo

## Day_19

- 01-Build-Todo-List-Web-App
    - Rehacemos la misma app de tareas, pero ahora como aplicación web
    - web.py
    - functions.py
    - dockerfile
    - run.sh
    - requirements.txt
    - pages/about.py
- 02-Bonus
    - Vamos a hacer una webapp que pueda encender la cámara web, capturar una imagen y convertirla a escala de grises o use otros filtros distintos
    - home.py
- 03-Exercise
    - Es el mismo ejercicio de trasnformación a grises, pero ahora lo hace a partir de una imagen que subimos
    - home.py
- NOTAS:
    - Vamos a usar `streamlit` para realizar una webapp
        - Se instala con el comando `pip install streamlit`
    - Para estas apps, si es muy importante acceder directamente a su carpeta, por ejemplo `Day_19/01-Build-Todo-List-Web-App` donde está el proyecto
    - Para ver la webapp en el navegador, hay que ir a la terminal y ejecutar `streamlit run <my_main_script>.py`
        - En mi webapp en concreto, hay que ejecutar `streamlit run web.py`
    - Al modificar código, hay que refrescar la página web para que esta se actualice
        - Se puede pulsar el botón de recargar del navegador, o, a la derecha, en la misma app, aparece también la opción de Rerun
    - La palabra clave `del` se usa para borrar objetos, y, como en Python todo es un objeto, sirve para borrar variables, listas, partes de una lista...
    - Aprendemos a hacer el deploy de una webapp realizada con streamlit en la nube de streamlit
        - Debemos crear un fichero `requirements.txt`
            - Para ello, ejecutar en la terminal, en la carpeta del proyecto el comando `pip freeze > requirements.txt`
            - Es un archivo que se subirá al servidor donde alojemos la webapp, para que el servidor conozca todas las bibliotecas de Python que tiene que instalar para poder ejecutar correctamente la webapp
        - Subimos el proyecto a Github
            - Habilitamos control de versiones Git para el proyecto y creamos un repositorio remoto en Github
        - En nuestro terminal volvemos a ejecutar nuestro proyecto con el comando `streamlit run web.py`
        - Como el proyecto está vinculado con Github, en el navegador donde tenemos nuestra app de todos ejecutándose aparecerá un menú que nos permite hacer el deploy de la webapp
            - Aparecerá un formulario donde hay que indicar el nombre del repositorio, la rama y el script principal a ejecutar (web.py en nuestro ejemplo). Indicamos estos tres valores y pulsamos el botón Deploy
        - Si todo va bien, aparecerá automáticamente nuestro proyecto
            - En mi caso: `https://josemanuelmunozmanzano-python-my-todo-app-webapp-web-gljb5o.streamlit.app/`
            - Si pulsamos en el botón `Manage app` situado abajo a la derecha, se ven los logs, por si tenemos algún problema con nuestra app
        - Acceder a `https://share.streamlit.io/` y hacer login con nuestro usuario para ver los proyectos desplegados
    - Para convertir una imagen a escala de grises necesitamos el paquete `pillow`
        - Se instaló como dependencia cuando instalamos streamlit
    - Para desplegar en mi Raspberry Pi 5
        - Seguir esta web: `https://medium.com/@dipikadhara06/python-streamlit-apps-development-with-docker-44b302040707`
        - Se ha creado un fichero `dockerfile`
        - Se ha creado un fichero ejecutable `run.sh`
            - Hacerlo ejecutable con el mandato: `chmod +x run.sh`
        - Se ha creado el fichero `requirements.txt` (ver arriba como generarlo)
        - Se ha pasado todo a mi Raspberry Pi 5, a la carpeta `projects`
        - Se ha creado un fichero `README.md` para saber como generar la imagen y ejecutar el contenedor
            - `docker build -t todo-app-streamlit:text .`
            - `docker run --rm -p 8502:8501 todo-app-streamlit:test`
        - Acceder a la ruta: `192.168.1.41:8502`

## Day_20

- Apuntes
    - Tanto en formato Pdf como Jupyter Notebook
    - Revision+Presentation.pynb
    - Revision+Presentation.pdf
- NOTAS:
    - En este día se hace un repaso de todo lo aprendido en los últimos 19 días
    - Se adjuntan apuntes en Pdf y en formato Jupyter Notebook

## Browser_Automation_And_Web_Scraping
- Hacemos scraping de un texto estático
    - example_01.py
- Hacemos scraping de un número dinámico
    - example_02.py
- Hacemos acciones en una página de login, mandando usuario y contraseña, pulsando Intro y haciendo click en el botón Home de la página a la que se accede tras el login
    - example_03.py
- Primer Ejercicio donde hacemos el login, pulsamos el botón home y recuperamos el número dinámico
    - exercise_01.py
- Segundo Ejercicio donde hacemos el login, pulsamos el botón home, y cada dos segundos recuperamos el número dinámico y lo guardamos en un nuevo fichero
    - exercise_02.py
- Tercer Ejercicio donde practicamos con otra web para cimentar los conocimientos de Scraping
    - Voy a ir a la página de Vaadin.com, hacer login con el mail / password y pulsar el href Whistleblowing
    - exercise_03.py
- Ejemplo donde aprendemos a descargar datos bursátiles históricos usando Python
    - La data la vamos a coger de `finance.yahoo.com`
    - Se van a hacer HTTP requests
    - Aunque no se usa en el programa, se indica como transformar una fecha string a epoch
    - example_04.py
- Usamos Beautiful Soup para hacer scraping de una página y obtener el valor de cambio de una moneda
    - Más adelante en el curso (versión GUI) haremos una app de escritorio para poder seleccionar las monedas
    - example_05.py
- NOTAS:
    - Selenium es una biblioteca de Python de terceros que se utiliza para automatizar acciones del navegador
        - Documentación: `https://www.selenium.dev/documentation/`
    - En esta automatización vamos a hacer scraping de una página web
        - Para obtener texto estático y el número dinámico: `http://automated.pythonanywhere.com`
        - Para hacer acciones en el login: `http://automated.pythonanywhere.com/login/`
            - usuario: automated
            - password: automatedautomated
    - Para instalar Selenium: `pip install selenium`
    - La web de Selenium WebDriver es: `https://www.selenium.dev/documentation/webdriver/`
    - WebDriver es una herramienta que nos permite instruir el comportamiento del navegador web, y tenemos acceso a WebDriver desde Python usando Selenium
    - Y para descargar el driver para Selenium en los distintos navegadores: `https://www.selenium.dev/selenium/docs/api/py/index.html#drivers`
        - Se necesita saber qué versión de navegador tenemos. Para ello acceder a: `https://www.whatismybrowser.com/`
        - En Ubuntu no he tenido que instalar ningún driver, pero es porque Selenium 4 lo hace todo automáticamente y ya no hace falta el driver
    - Si el valor que queremos scrapear no aparece hasta pasado un tiempo, podemos usar la librería `time` y el método `sleep(2)` donde 2 son los segundos que espera
        - Documentación: `https://docs.python.org/3/library/time.html`
    - En vez de `time`, si necesitamos esperar a que aparezca un botón, es mejor importar `from selenium.webdriver.support.ui import WebDriverWait` y usar, por ejemplo:
        -  `WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/nav/div/a')))`
        - Documentación: `https://selenium-python.readthedocs.io/waits.html`
    - Para copiar un `Xpath` de una web:
        - Acceder al modo desarrollador
        - Buscar lo que queremos obtener con el scraping
        - Pulsar botón derecho en el inspector, seleccionar `Copiar/Xpath`
        - No siempre vamos a obtener el Xpath porque la estructura HTML puede ser complicada. En ese caso tendremos que usar la lógica
            - En Chrome tenemos la opción `Copy full Xpath` en el mismo menú donde tenemos `Xpath`
    - Si el elemento al que queremos acceder tiene un `id`, podemos usarlo también. Es la solución más robusta
    - Documentación datetime: `https://docs.python.org/3/library/datetime.html`
        - datetime.now() nos da la fecha/hora actual
        - Su tipo es datetime
    - Documentación para hacer click en un checkbox que verifica si eres humano
        - `https://stackoverflow.com/questions/76575298/how-to-click-on-verify-you-are-human-checkbox-challenge-by-cloudflare-using-se.`
    - Documentación para enviar HTTP/1.1 requests y descargar ficheros
        - `https://docs.python-requests.org/en/latest/`
    - Aprendemos también a usar Beautiful Soup para hacer scraping de una página
        - La diferencia entre Selenium y Beautiful Soup es que Selenium se usa más para automatizaciones del navegador, mientras que Beautiful Soup se usa solo para extraer data de una web (puro scraping, sin abrir el navegador siquiera)
        - Beautiful Soup está hecho para entender la estructura HTML
        - Instalar con el comando: `pip install beautifulsoup4`

## Accessing APIs | Building APIs
- En esta sección usaremos Python para acceder a varias APIs y crearemos nuestra propia API
- Para estos ejemplos, sustituir el nombre `API_KEY_template.txt` por `API_KEY.txt` e indicar la API KEY donde se indica `<mykey>`
    - example_01.py
        - Accederemos a los principales titulares de un topic en unas fechas concretas y en un idioma
    - example_02.py
        - Accederemos a los principales titulares de un país en particular
- NOTAS:
    - En concreto vamos a trabajar con REST APIs, que son las más comunes
    - Obtenemos la API key de la web siguiente: `https://newsapi.org/`
    - Documentación sobre requests: `https://docs.python-requests.org/en/latest/`
        - Utilizamos esta librería para acceder a las APIs externas

