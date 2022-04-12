import tkinter as tk #Esta libreria nos permite crear interfaces
from pygame import mixer #Importamos el modulo para que sea mas facil de utilizar las herramientas
import mutagen #Permite obtener la duración de la canción
import os #Este nos proporciona funciones para crear y eliminar un directorio, recuperar su contenido, etc.
import fnmatch #Este módulo proporciona soporte para comodines de estilo shell de Unix, nos ayuda a identificar las extenciones en consola
mixer.init()#Iniciamos el reproductor
mixer.music.set_volume(0.7)
cancion = ''#Apartir de aqui modificamos los parametros ;)
canvas = tk.Tk()
canvas.title("Reproductor de musica de TomiCat")
canvas.geometry("800x500")
canvas.config(bg='black')
canvas.mainloop()
#Estos son algunos de los modulos que posiblemente me ayuden, pero almenos hice mi primera ventana xd