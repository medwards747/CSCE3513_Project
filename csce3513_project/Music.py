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
        self.win = Tk()
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

        # add background
        im = tkinter.PhotoImage(
            file="csce3513_project/images/lazer_tag_bg.png")
        # im_bg = Label(win, image=im)
        # im_bg.pack()

        self.canvas = Canvas(self.win)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=im, anchor="nw")

        top = Frame(self.win).pack(side=TOP)
        heading = Label(top, text="Select the Music Track",
                        font=('Times', 50)).pack(pady=30)
        left = Frame(self.win, bg='black')
        left.pack(side=LEFT, padx=50)
        middle = Frame(self.win, bg='black')
        middle.pack(side=LEFT, padx=50)
        right = Frame(self.win, bg='black')
        right.pack(side=LEFT, padx=30)

        # create all buttons
        self._button_1 = Button(left, text='Track 1', font=('Times', 32))
        self._button_1.config(
            command=lambda obj=self._button_1: self.clicked(obj))
        self._button_1.bind('<<Track 1 Selected>>', self.clicked)
        self._button_1.pack(padx=30, pady=30)

        self._button_2 = Button(left, text='Track 2', font=('Times', 32))
        self._button_2.config(
            command=lambda obj=self._button_2: self.clicked(obj))
        self._button_2.bind('<<Track 2 Selected>>', self.clicked)
        self._button_2.pack(padx=30, pady=30)

        self._button_3 = Button(left, text='Track 3', font=('Times', 32))
        self._button_3.config(
            command=lambda obj=self._button_3: self.clicked(obj))
        self._button_3.bind('<<Track 3 Selected>>', self.clicked)
        self._button_3.pack(padx=30, pady=30)

        self._button_4 = Button(middle, text='Track 4', font=('Times', 32))
        self._button_4.config(
            command=lambda obj=self._button_4: self.clicked(obj))
        self._button_4.bind('<<Track 4 Selected>>', self.clicked)
        self._button_4.pack(padx=30, pady=30)

        self._button_5 = Button(middle, text='Track 5', font=('Times', 32))
        self._button_5.config(
            command=lambda obj=self._button_5: self.clicked(obj))
        self._button_5.bind('<<Track 5 Selected>>', self.clicked)
        self._button_5.pack(padx=30, pady=30)

        self._button_6 = Button(middle, text='Track 6', font=('Times', 32))
        self._button_6.config(
            command=lambda obj=self._button_6: self.clicked(obj))
        self._button_6.bind('<<Track 6 Selected>>', self.clicked)
        self._button_6.pack(padx=30, pady=30)

        self._button_7 = Button(right, text='Track 7', font=('Times', 32))
        self._button_7.config(
            command=lambda obj=self._button_7: self.clicked(obj))
        self._button_7.bind('<<Track 7 Selected>>', self.clicked)
        self._button_7.pack(padx=30, pady=30)

        self._button_8 = Button(right, text='Track 8', font=('Times', 32))
        self._button_8.config(
            command=lambda obj=self._button_8: self.clicked(obj))
        self._button_8.bind('<<Track 8 Selected>>', self.clicked)
        self._button_8.pack(padx=30, pady=30)

        self.p = Button(right, text='pause', font=(
            'Times', 32), command=self.pause)
        self.p.pack(padx=30, pady=30)

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
