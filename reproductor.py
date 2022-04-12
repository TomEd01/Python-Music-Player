import tkinter as tk #Esta libreria nos permite crear interfaces
#from tkinter import * #Tal vez este comando va hacer que escriba otra vez el codigo xd
from pygame import mixer #Importamos el modulo para que sea mas facil de utilizar las herramientas
#import mutagen #Permite obtener la duración de la canción
import os #Este nos proporciona funciones para crear y eliminar un directorio, recuperar su contenido, etc.
import fnmatch #Este módulo proporciona soporte para comodines de estilo shell de Unix, nos ayuda a identificar las extenciones en consola

mixer.init()#Iniciamos el reproductor
mixer.music.set_volume(1)

#Apartir de aqui modificamos los parametros ;)
ubicacion = 'C:\\Users\TomiCat xD\Music\Musicaxd'
extencion = '*.mp3'

#Configuración principal de la ventana de windos
ventana = tk.Tk()
ventana.title("Reproductor de musica de TomiCat")
ventana.geometry("800x500")
ventana.iconbitmap('icons/ico.ico')
ventana.config(bg='green')
ventana.resizable(0,0)

#Un poco de estilo de game-boy xd
lista = tk.Listbox(ventana, fg="black", bg='green',width=150, font=('Retro Gaming',12))
lista.pack(padx=15, pady=15)
#lista.insert(0,'musica 1 :0') #Con esto ingresamos algo en nuestra ventana
#Estilos que hacen la diferencia y/o volumen proximamente xd
espacio = tk.Label(ventana, text='',bg='green',fg='green', font=('Retro Gaming',14))
espacio.pack(pady=15)
#No me hagan caso jajaja
prev_img = tk.PhotoImage(file='icons/prev.png')
next_img = tk.PhotoImage(file='icons/next.png')
play_img = tk.PhotoImage(file='icons/play.png')
pause_img = tk.PhotoImage(file='icons/stop.png')
stop_img = tk.PhotoImage(file='icons/pause.png')
#Damos estilos generales a los botonos, es como una funcion
buttom_all = tk.Frame(ventana, bg='green')
buttom_all.pack(padx=10, pady=5,anchor='center')

#Creamos los botones con los estilos generales
previous = tk.Label(ventana,text='Anterior', image= prev_img, bg='green', borderwidth=0)
previous.pack(pady=15, in_=buttom_all, side='left')
stop = tk.Label(ventana, text='Detener', image=stop_img, bg='green', borderwidth=0)
stop.pack(pady=15, in_=buttom_all, side='left')
pause = tk.Label(ventana,text='Pausa', image= pause_img, bg='green', borderwidth=0)
pause.pack(pady=15, in_=buttom_all, side='left')
play = tk.Label(ventana, text='Continuar', image=play_img, bg='green', borderwidth=0)
play.pack(pady=15, in_=buttom_all, side='left')
nextB = tk.Label(ventana, text='Siguiente', image=next_img, bg='green', borderwidth=0)
nextB.pack(pady=15, in_=buttom_all, side='left')
#Ingresamos todos los archivos .mp3 de la carpeta que declaramos
for root, dirs, archivos in os.walk(ubicacion): 
    for nom_archivo in fnmatch.filter(archivos,extencion):
        lista.insert('end', nom_archivo)
ventana.mainloop()
#Aqui le di estilos a mi ventana tipo game-boy