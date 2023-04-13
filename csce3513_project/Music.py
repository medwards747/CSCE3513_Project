import tkinter
from tkinter import *
import pygame
from pygame import mixer
import os
from PIL import Image, ImageTk


class musicPlay():

    # get length of mp3 file
    def get_len(self, file):
        i = pygame.mixer.Sound(file)
        a = i.get_length()
        return (a)

    # set start time of mp3 file
    def set_len(self, file):
        '''
        Each mp3 file has different features and music start times.
        This function hard codes in different cuts for each mp3 file.
        '''

        if file == self.track_paths[4]:
            return (self.get_len(file) - 30)
        elif (file == self.track_paths[5] or file == self.track_paths[6]):
            return (self.get_len(file) / 3)
        else:
            return (300)

    # plays mp3 file
    def play(self, file):
        mixer.music.load(file)
        mixer.music.play(-1, start=self.set_len(file))

    # pause all music from all channels
    def pause(self):
        pygame.mixer.music.pause()

    def get_selection(self):
        return self.selection

    # register a Button being pressed
    def clicked(self, widget):
        chosenTrack = "Random"
        if widget == self._button_1:
            print('Track 1')
            chosenTrack = "Track 1"
            self.selection = 0
            self.play(self.track_paths[0])
        elif widget == self._button_2:
            print('Track 2')
            chosenTrack = "Track 2"
            self.selection = 1
            self.play(self.track_paths[1])
        elif widget == self._button_3:
            print('Track 3')
            chosenTrack = "Track 3"
            self.selection = 2
            self.play(self.track_paths[2])
        elif widget == self._button_4:
            print('Track 4')
            chosenTrack = "Track 4"
            self.selection = 3
            self.play(self.track_paths[3])
        elif widget == self._button_5:
            print('Track 5')
            chosenTrack = "Track 5"
            self.selection = 4
            self.play(self.track_paths[4])
        elif widget == self._button_6:
            print('Track 6')
            chosenTrack = "Track 6"
            self.selection = 5
            self.play(self.track_paths[5])
        elif widget == self._button_7:
            print('Track 7')
            chosenTrack = "Track 7"
            self.selection = 6
            self.play(self.track_paths[6])
        elif widget == self._button_8:
            print('Track 8')
            chosenTrack = "Track 8"
            self.selection = 7
            self.play(self.track_paths[7])
        return chosenTrack

    def show_gui(self) -> None:
        # creates music selection window
        self.win = Toplevel()
        self.win.title("Music Selection")

        # Start 1st track
        self.play(self.track_paths[0])

        width, height = 1000, 700
        screen_width = self.win.winfo_screenwidth()
        screen_height = self.win.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (width / 2)
        y_coordinate = (screen_height / 2) - (height / 2)

        # adjust where it pops up
        self.win.geometry("%dx%d+%d+%d" %
                          (width, height, x_coordinate, y_coordinate))


        im = Image.open("csce3513_project/images/lazer_tag_bg.png")
        render = ImageTk.PhotoImage(im)

        self.bg = Label(self.win, image=render)
        self.bg.image = render

        self.bg.grid(row=0, column=0, rowspan=2, columnspan=3)

        # initialize music player
        pygame.init()

        # list all music tracks
        tracks = os.listdir('csce3513_project/photon_tracks')
        print(tracks)
        self.path = ['csce3513_project/photon_tracks/' + i for i in tracks]
        print(self.path)
        # default music selection
        pygame.mixer.music.load(self.path[0])
        pygame.mixer.music.play(start=300)

        self.win.grid_rowconfigure(0, weight=1)
        self.win.grid_rowconfigure(1, weight=3)
        self.win.grid_columnconfigure(0, weight=1)
        self.win.grid_columnconfigure(1, weight=1)
        self.win.grid_columnconfigure(2, weight=1)

        top = Frame(self.win).grid(row=0)
        heading = Label(top, text="Select the Music Track", font=('Times', 50), fg='dark blue')
        heading.grid(row=0, column=0,columnspan=3,sticky='NSEW')
        left = Frame(self.win, bg='dark blue')
        left.grid(row=1, column=0, padx=5, pady=100, sticky='NS')
        middle = Frame(self.win, bg='dark blue')
        middle.grid(row=1, column=1, padx=5, pady=100, sticky='NS')
        right = Frame(self.win, bg='dark blue')
        right.grid(row=1, column=2, padx=5, pady=100, sticky='NS')

        # create all buttons
        self._button_1 = Button(left, text='Track 1', font=('Times', 32), fg='dark blue', width=10)
        self._button_1.config(command=lambda obj=self._button_1: self.clicked(obj))
        self._button_1.bind('<<Track 1 Selected>>', self.clicked)
        self._button_1.grid(row=0, ipady=10, pady=10)

        self._button_2 = Button(left, text='Track 2', font=('Times', 32), fg='dark blue', width=10)
        self._button_2.config(command=lambda obj=self._button_2: self.clicked(obj))
        self._button_2.bind('<<Track 2 Selected>>', self.clicked)
        self._button_2.grid(row=1, ipady=10, pady=10)

        self._button_3 = Button(left, text='Track 3', font=('Times', 32), fg='dark blue', width=10)
        self._button_3.config(command=lambda obj=self._button_3: self.clicked(obj))
        self._button_3.bind('<<Track 3 Selected>>', self.clicked)
        self._button_3.grid(row=2, ipady=10, pady=10)

        self._button_4 = Button(middle, text='Track 4', font=('Times', 32), fg='dark blue', width=10)
        self._button_4.config(command=lambda obj=self._button_4: self.clicked(obj))
        self._button_4.bind('<<Track 4 Selected>>', self.clicked)
        self._button_4.grid(row=0, ipady=10, pady=10)

        self._button_5 = Button(middle, text='Track 5', font=('Times', 32), fg='dark blue', width=10)
        self._button_5.config(command=lambda obj=self._button_5: self.clicked(obj))
        self._button_5.bind('<<Track 5 Selected>>', self.clicked)
        self._button_5.grid(row=1, ipady=10, pady=10)

        self._button_6 = Button(middle, text='Track 6', font=('Times', 32), fg='dark blue', width=10)
        self._button_6.config(command=lambda obj=self._button_6: self.clicked(obj))
        self._button_6.bind('<<Track 6 Selected>>', self.clicked)
        self._button_6.grid(row=2, ipady=10, pady=10)

        self._button_7 = Button(right, text='Track 7', font=('Times', 32), fg='dark blue', width=10)
        self._button_7.config(command=lambda obj=self._button_7: self.clicked(obj))
        self._button_7.bind('<<Track 7 Selected>>', self.clicked)
        self._button_7.grid(row=0, ipady=10, pady=10)

        self._button_8 = Button(right, text='Track 8', font=('Times', 32), fg='dark blue', width=10)
        self._button_8.config(command=lambda obj=self._button_8: self.clicked(obj))
        self._button_8.bind('<<Track 8 Selected>>', self.clicked)
        self._button_8.grid(row=1, ipady=10, pady=10)

        self.p = Button(right, text='pause', font=('Times', 32), command=self.pause, fg='dark blue', width=10)
        self.p.grid(row=2, ipady=10, pady=10)

        self.win.mainloop()
     
        # Stop the music
        pygame.mixer.music.stop()

    def __init__(self, track: int, autoplay=True) -> None:
        # initialize music player
        pygame.init()
        self.selection = None

        # list all music tracks
        track_dir = 'csce3513_project/photon_tracks/'
        tracks = os.listdir(track_dir)
        self.track_paths = [track_dir + i for i in tracks]
        # default music selection
        pygame.mixer.music.load(self.track_paths[track])
        if autoplay:
            pygame.mixer.music.play()

