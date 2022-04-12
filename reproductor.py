from pydoc import text
import tkinter as tk #Esta libreria nos permite crear interfaces
from pygame import mixer #Importamos el modulo para que sea mas facil de utilizar las herramientas
#import mutagen #Permite obtener la duración de la canción
import os #Este nos proporciona funciones para crear y eliminar un directorio, recuperar su contenido, etc.
import fnmatch #Este módulo proporciona soporte para comodines de estilo shell de Unix, nos ayuda a identificar las extenciones en consola

mixer.init()#Iniciamos el reproductor
volumen_general = float(.5)
mixer.music.set_volume(volumen_general)

#Apartir de aqui modificamos los parametros ;)
ubicacion = 'C:\\Users\TomiCat xD\Music\Musicaxd'
extencion = '*.mp3'

#Funciones que mandamos a llamar desde los botones
def reproducir():
    textadd = lista.get('anchor')
    espacio.config(text=textadd)
    mixer.music.load(ubicacion + '\\' + textadd)
    mixer.music.play()
    volumen_label.config(fg="black",text="Volume : " + str(volumen_general))
def detener():
    mixer.music.stop()
    ventana.destroy()#Esta bien escrito pero al ejecutarlo da error, posiblemente un bug
    lista.select_clear('active')
def siguiente():#Hacemos que avance
    sig_music = lista.curselection()
    sig_music = sig_music[0]+1
    sig_music_nom = lista.get(sig_music)
    espacio.config(text=sig_music_nom)
    #Colocomos la ruta de la canción que avanzamos
    mixer.music.load(ubicacion + '\\' + sig_music_nom)
    mixer.music.play()
    #borramos la posición anterior y la remplazamos con la actual
    lista.select_clear(0,'end')
    lista.activate(sig_music)
    lista.select_set(sig_music)
def pausa():#Esto lo hice por si quieren utilizar el boton de pausa como play xD
    if pause['text']=='pause':
        mixer.music.pause()
        pause['text'] = 'play'
    else:
        mixer.music.unpause()
        pause['text'] = 'pause'
def anterior():
    sig_music = lista.curselection()
    sig_music = sig_music[0]-1 #Lo mismo, solo que indicamos que retroceda
    sig_music_nom = lista.get(sig_music)
    espacio.config(text=sig_music_nom)
    #Colocomos la ruta de la canción que avanzamos
    mixer.music.load(ubicacion + '\\' + sig_music_nom)
    mixer.music.play()
    #borramos la posición anterior y la remplazamos con la actual
    lista.select_clear(0,'end')
    lista.activate(sig_music)
    lista.select_set(sig_music)
def menos_volumen():
    global volumen_general
    if volumen_general <= 0:
        volumen_label.config(fg="red", text="Volumen : Silencio")
        return
    volumen_general = volumen_general - float(0.1) 
    volumen_general = round(volumen_general,1)
    mixer.music.set_volume(volumen_general)
    volumen_label.config(fg="black", text="Volume : "+str(volumen_general))
def mas_volumen():
    global volumen_general
    if volumen_general >=1:
        volumen_label.config(fg="yellow", text="Volumen : Maximo")
        return
    volumen_general = volumen_general + float(0.1) 
    volumen_general = round(volumen_general,1)
    mixer.music.set_volume(volumen_general)
    volumen_label.config(fg="black", text="Volume : "+str(volumen_general))
#Configuración principal de la ventana de windos
ventana = tk.Tk()
ventana.title("Reproductor de musica de TomiCat")
ventana.geometry("800x550")
ventana.iconbitmap('icons/ico.ico')
ventana.config(bg='green')
ventana.resizable(0,0)

#Un poco de estilo de game-boy xd
lista = tk.Listbox(ventana, fg="black", bg='green',width=150, font=('Retro Gaming',12))
lista.pack(padx=15, pady=15)

#Estilos que hacen la diferencia y/o volumen proximamente xd
espacio = tk.Label(ventana, text='',bg='green',fg='black', font=('Retro Gaming',14))
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
previous = tk.Button(ventana,text='Anterior', image= prev_img, bg='green', borderwidth=0, command=anterior)
previous.pack(pady=15, in_=buttom_all, side='left')
stop = tk.Button(ventana, text='Detener', image=stop_img, bg='green', borderwidth=0, command=detener)
stop.pack(pady=15, in_=buttom_all, side='left')
play = tk.Button(ventana, text='Continuar', image=play_img, bg='green', borderwidth=0, command=reproducir)
play.pack(pady=15, in_=buttom_all, side='left')
pause = tk.Button(ventana,text='Pausa', image= pause_img, bg='green', borderwidth=0)
pause.pack(pady=15, in_=buttom_all, side='left')
nextB = tk.Button(ventana, text='Siguiente', image=next_img, bg='green', borderwidth=0, command=siguiente)
nextB.pack(pady=15, in_=buttom_all, side='left')
volumen_label = tk.Label(ventana,font=('Retro Gaming',12),bg='green')
volumen_label.pack(pady=5)
volumen_buttom_mas = tk.Button(ventana, text='+',font=('Retro Gaming',12),width=2,command=mas_volumen,bg='green')
volumen_buttom_mas.pack(pady=5, side='right')
volumen_buttom_menos = tk.Button(ventana, text='-',font=('Retro Gaming',12),width=2,command=menos_volumen,bg='green')
volumen_buttom_menos.pack(pady=5, side='right')
#Ingresamos todos los archivos .mp3 de la carpeta que declaramos
for root, dirs, archivos in os.walk(ubicacion): 
    for nom_archivo in fnmatch.filter(archivos,extencion):
        lista.insert('end', nom_archivo)
ventana.mainloop()
#Ya le di funcionalida