from email.mime import audio
from tkinter import *
from os import system
from turtle import left
import pygame
from tkinter import filedialog
import wave
from clip import *
import librosa
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('SoundDeep')
root.geometry("500x400")
menu = Menu(root, tearoff=False)
root.config(menu=menu)
subMenu = Menu(root, tearoff=False)
menu.add_cascade(label="File", menu=subMenu)
pygame.init()
audioFile = None

def playOriginal():
  global audioFile
  print(audioFile)
  if (audioFile != None):
    pygame.mixer.music.load(audioFile)
    pygame.mixer.music.play(loops=0)
  else: 
    createAlert()

def spectogram():
  y,sr = librosa.load(audioFile, duration=30)
  S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000, hop_length=((1 + np.array(y).shape[0]) // 64), n_fft=2048)
  fig = plt.Figure()
  #canvas = FigureCanvas(fig)
  plt.imshow(librosa.power_to_db(S,ref=np.max))
  plt.show()

def stopOriginal():
  pygame.mixer.music.stop()

def stopCutVersion():
  pygame.mixer.music.stop()

def loadAudio():
  global audioFile
  filename = filedialog.askopenfilename(initialdir="/Images", title="Select a File", filetypes=[('Wav files', '*.wav'), ('Mp3 files', '*.mp3')])
  #audio = wave.open(filename)
  audioFile = filename
  generateFeaturedClip(audioFile, 30)
  spectogram()

def playCutVersion():
  if (audioFile != None):
    pygame.mixer.music.load('best-moment.wav')
    pygame.mixer.music.play(loops=0)
  else: 
    createAlert()

def createAlert():
  alert = Toplevel(root)
  window_height = 100
  window_width = 250
  screen_width = root.winfo_screenwidth()
  screen_height = root.winfo_screenheight()
  x_cordinate = int((screen_width/2) - (window_width/2))
  y_cordinate = int((screen_height/2) - (window_height/2))
  alert.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate - 200))
  alertLabel = Label(alert,text="Please load a song")
  alertLabel.pack()
  alert.after(5000, lambda: alert.destroy())
  alert.mainloop()
  
def quitr():
  root.quit()
  root.destroy()
  exit()

main_frame = Frame(root, width=500, height=250)
main_frame.pack()
originalLabel = Label(main_frame, text="Original song: ",font=("Helvetica",12))
originalLabel.place(x=50,y=20)
play_button = Button(root, text="Play song  ", font=("Helvetica", 16), command=playOriginal)
play_button.place(x=180,y=10)
stop_button = Button(root, text="Stop sound", font=("Helvetica", 16), command=stopOriginal)
stop_button.place(x=320,y=10)
clipLabel = Label(main_frame, text="Clipped song: ",font=("Helvetica",12))
clipLabel.place(x=50,y=160)
clip_button = Button(root, text="Play clip  ", font=("Helvetica", 16), command=playCutVersion)
clip_button.place(x=180,y=140)
clip_stop_button = Button(root, text="Stop clip", font=("Helvetica", 16), command=stopCutVersion)
clip_stop_button.place(x=320,y=140)
subMenu.add_command(label="Load", command=loadAudio)
root.mainloop()
root.protocol("WM_DELETE_WINDOW", quitr)