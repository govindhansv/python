from tkinter import *
from pygame import mixer
import os



def playsong():
    currentsong = playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    mixer.music.play()
def pausesong():
    mixer.music.pause()
def stopsong():
    mixer.music.stop()
def resumesong():
    mixer.music.unpause()


root = Tk()

root.geometry("700x350")
root.title('music player')







mixer.init()
playlist = Listbox(root,selectmode=SINGLE,bg = '#EFEFD0', width=100, height=15)
playlist.grid(columnspan =5)
os.chdir("./songs/")
song = os.listdir()
for s in song:
    playlist.insert(END,s)



Button(root,text= 'play', command = playsong, height= 2, width=10).grid(row =1 , column = 0)
Button(root,text= 'pause', command = pausesong, height= 2, width=10).grid(row =1 , column = 1)
Button(root,text= 'stop', command = stopsong, height= 2, width=10).grid(row =1 , column = 2)
Button(root,text= 'resume', command = resumesong, height= 2, width=10).grid(row =1 , column = 3)



mainloop()