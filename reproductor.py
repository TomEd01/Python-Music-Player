from pygame import mixer #Importamos el modulo para que sea mas facil de utilizar las herramientas
mixer.init()#Iniciamos el reproductor
cancion = str(input("Selecione la canción "))#Apartir de aqui modificamos los parametros ;)
mixer.music.load(cancion)#Escribimos el nombre de la canción junto con la extención
mixer.music.set_volume(0.7)
mixer.music.play()
while True:#Hacemos esta condición para que nos pueda dar siempre una opcción
    print("Pulsa p para pausar la canción")
    print("Pulsa r para reproducir la canción")
    print("Pulsa e para elegir otra canción")
    print("Pulsa s para salir")
    opccion = input(">>>>>> ")#Ingresamos las opcciones
    if opccion == "p":
        mixer.music.pause()#Pausamos musica
    elif opccion == "r":
        mixer.music.unpause()#Reproducimos musica
    elif opccion == "s":
        mixer.music.stop()#Cerramos la musica y nos salimos del menu de opcciónes
        exit()
    elif opccion == "e":#Configuramos para la siguiente musica
        mixer.music.stop()
        cancion = str(input("Selecione la canción"))
        mixer.music.load(cancion)
        mixer.music.set_volume(0.7)
        mixer.music.play()
#Se que esto es basico, pero almenos me ayuda a entender que me viene en mi futuro