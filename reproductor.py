import tkinter as tk #Esta libreria nos permite crear interfaces
from tkinter import Frame, Menu,ttk,filedialog,messagebox #Algunos componentes utiles
from pygame import mixer #Importamos el modulo para que sea mas facil de utilizar las herramientas
import mutagen #Permite obtener la duración de la canción
import os #Este nos proporciona funciones para crear y eliminar un directorio, recuperar su contenido, etc.
import fnmatch #Este módulo proporciona soporte para comodines de estilo shell de Unix, nos ayuda a identificar las extenciones en consola
from PIL import Image,ImageTk #Trabajar mas facil con imagenes

mixer.init()#Iniciamos el reproductor
volumen_general = float(.5)
mixer.music.set_volume(volumen_general)

#Apartir de aqui modificamos los parametros ;)
def directorio():
    global  ubicacion,extencion
    lista.delete(0,'end')
    direccion = filedialog.askdirectory()
    ubicacion = direccion
    extencion = '*.mp3'
    for root, dirs, archivos in os.walk(ubicacion): 
        for nom_archivo in fnmatch.filter(archivos,extencion):
            lista.insert('end', nom_archivo)
ubicacion = '' #C:\\Users\TomiCat xD\Music\Musicaxd

#Funciones que mandamos a llamar desde los botones
def creador():
    messagebox.showinfo('Sobre la app',"Esta app fue creada por Edwin Tomas alias TomiCat visita mi repositorio https://github.com/TomEd01/Python-Music-Player para ver la documentación")
def tiempos(ub):
    audio = mutagen.File(ub)
    largo = audio.info.length
    minutos, segundos = divmod(largo, 60)
    minutos, segundos = int(minutos), int(segundos)
    tiempo_label['text']= str(minutos) + ":" + str(segundos)
def reproducir():
    if play['text']=='Reproducir':
        textadd = lista.get('anchor')
        espacio.config(text=textadd)
        ub = ubicacion + '\\' + textadd
        mixer.music.load(ub)
        mixer.music.play()
        tiempos(ub)
        volumen_label.config(fg="black",text="Volume : " + str(volumen_general))
        play['text']='pause'
    elif play['text']=='pause':
        mixer.music.pause()
        play['text'] = 'Reproducir'
    else:
        mixer.music.unpause()
        play['text'] = 'Reproducir'
def detener():
    mixer.music.stop()
    ventana.quit()
    lista.select_clear('active')
def siguiente():#Hacemos que avance
    sig_music = lista.curselection()
    sig_music = sig_music[0]+1
    sig_music_nom = lista.get(sig_music)
    espacio.config(text=sig_music_nom)
    #Colocomos la ruta de la canción que avanzamos
    ub = ubicacion + '\\' + sig_music_nom
    mixer.music.load(ub)
    mixer.music.play()
    #borramos la posición anterior y la remplazamos con la actual
    lista.select_clear(0,'end')
    lista.activate(sig_music)
    lista.select_set(sig_music)
    tiempos(ub)
def anterior():
    sig_music = lista.curselection()
    sig_music = sig_music[0]-1
    sig_music_nom = lista.get(sig_music)
    espacio.config(text=sig_music_nom)
    #Colocomos la ruta de la canción que avanzamos
    ub = ubicacion + '\\' + sig_music_nom
    mixer.music.load(ub)
    mixer.music.play()
    #borramos la posición anterior y la remplazamos con la actual
    lista.select_clear(0,'end')
    lista.activate(sig_music)
    lista.select_set(sig_music)
    tiempos(ub)
def menos_volumen():
    global volumen_general
    if volumen_general <= 0:
        volumen_label.config(fg="orange", text="Volumen : Silencio")
        return
    volumen_general = volumen_general - float(0.1) 
    volumen_general = round(volumen_general,1)
    mixer.music.set_volume(volumen_general)
    volumen_label.config(fg="black", text="Volume : "+str(volumen_general))
def mas_volumen():
    global volumen_general
    if volumen_general >=1:
        volumen_label.config(fg="red", text="Volumen : Maximo")
        return
    volumen_general = volumen_general + float(0.1) 
    volumen_general = round(volumen_general,1)
    mixer.music.set_volume(volumen_general)
    volumen_label.config(fg="black", text="Volume : "+str(volumen_general))
#Configuración principal de la ventana de windos
ventana = tk.Tk()
ventana.title("Reproductor de musica de TomiCat")
ventana.geometry("820x550")
ventana.iconbitmap('icons/ico.ico')
ventana.resizable(0,0)

#Cajas
caja1 = Frame(ventana, bg='#F7F5F2',width=850,height=400)#Aqui se muestra la imagen y la lista
caja1.grid(row=0,column=0,sticky='nsew')
caja2= Frame(ventana, bg='#F7F5F2',width=820,height=150)#Aqui los controles
caja2.grid(row=1,column=0,sticky='nsew')

#Pestañas de configuración
menu = Menu(ventana)
ventana.config(bg='#F7F5F2',menu=menu)
Carpeta = Menu(menu, tearoff=0)
Carpeta.add_command(label='Nuevo directorio', command=directorio)
Carpeta.add_separator()
Carpeta.add_command(label='Acerca de', command=creador)
menu.add_cascade(label='Carpeta', menu=Carpeta)

#Un poco de estilo
scrollbar = ttk.Scrollbar(caja1, orient=tk.VERTICAL)
lista = tk.Listbox(caja1, fg="black", bg='#F7F5F2',width=51, height=22, font=('Roboto',11),borderwidth=0,yscrollcommand=scrollbar.set)
lista.grid(row=0,column=1)
img = Image.open('./icons/rc.jpg')
img= ImageTk.PhotoImage(img)
label_img = tk.Label(caja1, image=img,height=400, width=400)
label_img.grid(row=0,column=0)

#Estilos que hacen la diferencia y/o volumen proximamente xd
espacio = tk.Label(caja2, text='',bg='#F7F5F2',fg='black', font=('Roboto',14),width=55)
espacio.grid(row=0,column=2,columnspan=2,pady=10)
tiempo_label = tk.Label(caja2, text='',bg='#F7F5F2',fg='black', font=('Roboto',14))
tiempo_label.grid(row=0,column=4,columnspan=2,pady=10)
#No me hagan caso jajaja
prev_img = tk.PhotoImage(file='icons/prev.png')
next_img = tk.PhotoImage(file='icons/next.png')
play_img = tk.PhotoImage(file='icons/play.png')
stop_img = tk.PhotoImage(file='icons/stop.png')

#Creamos los botones con los estilos generales
previous = tk.Button(caja2,text='Anterior', image= prev_img, bg='#F7F5F2', borderwidth=0, relief="flat", command=anterior, cursor="hand1")
previous.grid(pady=10, row=1,column=1)
stop = tk.Button(caja2, text='Detener', image=stop_img, bg='#F7F5F2', borderwidth=0, relief="flat", command=detener, cursor="hand1")
stop.grid(pady=10, row=1,column=3)
play = tk.Button(caja2, text='Reproducir', image=play_img, bg='#F7F5F2', borderwidth=0, relief="flat", command=reproducir, cursor="hand1")
play.grid(pady=10, row=1,column=2)
nextB = tk.Button(caja2, text='Siguiente', image=next_img, bg='#F7F5F2', borderwidth=0, relief="flat", command=siguiente, cursor="hand1")
nextB.grid(pady=10, row=1,column=4)
volumen_label = tk.Label(caja2,font=('Roboto',12),bg='#F7F5F2')
volumen_label.grid(row=0,column=0,columnspan=2)
volumen_buttom_mas = tk.Button(caja2, text='+',font=('Roboto',16),width=2,command=mas_volumen,bg='#F7F5F2',relief="flat", cursor="hand1")
volumen_buttom_mas.grid(row=1,column=0,pady=15,padx=15)
volumen_buttom_menos = tk.Button(caja2, text='-',font=('Retro Gaming',16),width=2,command=menos_volumen,bg='#F7F5F2',relief="flat", cursor="hand1")
volumen_buttom_menos.grid(row=1,column=5,pady=15,padx=15)

#Ingresamos todos los archivos .mp3 de la carpeta que declaramos
if ubicacion == '':
    lista.insert('end', 'Coloca un nuevo directorio')
    lista.insert('end','Selecciona la pestaña carpeta')
else:
    for root, dirs, archivos in os.walk(ubicacion): 
        for nom_archivo in fnmatch.filter(archivos,extencion):
            lista.insert('end', nom_archivo)
ventana.mainloop()