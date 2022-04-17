# Introducción
Este reproductor fue basado en la biblioteca [tkinter](https://docs.python.org/es/3/library/tkinter.html) para implementar una interfaz visual moderna y llamar a bibliotecas de terceros como [pygame](https://www.pygame.org/docs/) para implementar funciones básicas como reproducir canciones, cambiar canciones e importar bibliotecas de múseica por lotes. 

El programa está configurado en ciclo único Modo, debe cambiar manualmente las canciones, también puede volver a definir la lista de reproducción e importar audio mp3 local.

## Instucciones
En caso de que seas un programador y quieras ejecutarlo desde tu editor o simplemente deseas saber como funciona, deberas instalar algunas librerias desde consola ya sea desde git bash o consola de tu sistema operativo y los comandos basicos son:

`pip install` *Nombre de la libreria*

Ahora si eres un usuario que quieres probar esta app, deberas descargar el proyecto tal cual, **La unica modificación que haras es crear un acceso directo** y ese archivo lo pondras en el escritorio o en donde tu gustes y lo ejecutaras como cualquier otro programa.

## ¿Como se que necesito instalar una libreria?
Bueno si tienes visual studio code y la configuraciíon necesaria para python, por defecto te lo mostrara los errores en las primeras lineas, dependiendo de que lineas sean necesitaras instalar esas librerias con el anterior codigo.

Cuando termines de instalar las librerias que te daban error, en ese momento cerraras la ventana de visual studio y volver a entrar para que aplique los cambios, si en este caso te sigue dando errores, debes darte una vuelta en algunos tutuoriales de YouTube o incluso puedes insertar el siguiente comando para actualiza el metodo de instalación e importaciones de modulos de python.

### Ejecuta los comandos segun su orden

- `python -m pip install -pgrade pip`

- `python -m pip install -upgrade pip`

- `pip --version`

## Que aprendi
Bueno, mas que nada aprendi a como utilizar ventanas en python ~~demanera basica obvio~~, pero como veran en mi primer commit no fue tal cual en ventana, si no en consola.

Ya que queria ver/conocer los conceptos basicos de el modulo de **pygames** y la importación de [mixer](https://www.pygame.org/docs/ref/mixer.html), no utilice mucho como tal pygames, si no la extencion/modulo de **mixer** ya que como dice su documentación que es para:

>Cargar y reproducir sonidos

Y con esto en la cabeza lo pude hacer, aun que luego me di cuenta que ya estaba el codigo hecho, pero aun asi fue genial la lluvia de ideas.

## Librerias
| **Nombre**  | **Descripcción**  |
| ------------ | ------------ |
| `pygame`   | Permite la creación de videojuegos en dos dimensiones de una manera sencilla al igual provee varios modulos |
| `mixer()`  | Este módulo contiene clases para cargar objetos de sonido y controlar la reproducción.  |
| `os()`  | Es posible realizar automáticamente muchas tareas del sistema operativo,proporciona funciones para crear y eliminar un [directorio](https://docs.python.org/es/3.10/library/os.html#module-os), recuperar su contenido, cambiar e identificar el directorio actual, etc.  |
| `tkinter()`  | Es el único [kit](https://docs.python.org/es/3/library/tkinter.html) de herramientas de interfaz gráfica de usuario multiplataforma (Windows, Mac, Unix) diseñado exclusivamente para lenguajes dinámicos de alto nivel  |
| `fnmatch()`  | Nos ayuda a identificar las extenciones en consola tipo Unix [Mas Info](https://docs.python.org/es/3.8/library/fnmatch.html#module-fnmatch) |
| `mutagen()`  | [Mutagen](https://mutagen.readthedocs.io/en/latest/) es un módulo de Python para manejar metadatos de audio.  |
| `PIL()`  | [Pillow](http://pillow.readthedocs.org/en/latest/) es una librería gratuita que permite la edición de imágenes directamente desde Python.  |

## ¿Cual fue mi proceso?
- Primero que nada, queria comensar con algo super sencillo, con conceptos basicos.

- Despues de invesstigar decidi que las anteriores librerias serian las indicadas.

- Despues, me vi un [video](https://www.youtube.com/watch?v=YXPyB4XeYLA) para aprender a manejar la ventana de tkinder y si que me gusto.

- Luego me parecio bastante curioso hacer un diseño algo antiguo como un game-boy.

![](https://github.com/TomEd01/Python-Music-Player/blob/main/icons/app.png)

- Pero luego me decidi por uno mas moderno y mas yo, si saben a lo que me refiero.

- Ya con el boceto hecho, fue sencillo codificarlo.

- De todas manera habra un cambio mas, quiero agregarle la barra de tiempo de reproducción espero lograrlo.