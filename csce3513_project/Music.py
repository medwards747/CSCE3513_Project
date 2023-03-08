import tkinter
from tkinter import *
import pygame
from pygame import mixer
import os
from PIL import Image, ImageTk


# get length of mp3 file
def get_len(file):
    i = pygame.mixer.Sound(file)
    a = i.get_length()
    return (a)


# set start time of mp3 file
def set_len(file):
    '''
    Each mp3 file has different features and music start times.
    This function hard codes in different cuts for each mp3 file.
    '''

    if file == path[4]:
        return (get_len(file) - 30)
    elif (file == path[5] or file == path[6]):
        return (get_len(file) / 3)
    else:
        return (300)


# plays mp3 file
def play(file):
    mixer.music.load(file)
    mixer.music.play(-1, start=set_len(file))


# pause all music from all channels
def pause():
    pygame.mixer.music.pause()


# register a Button being pressed
def clicked(widget):
    if widget == _button_1:
        print('Track 1')
        play(path[0])
    elif widget == _button_2:
        print('Track 2')
        play(path[1])
    elif widget == _button_3:
        print('Track 3')
        play(path[2])
    elif widget == _button_4:
        print('Track 4')
        play(path[3])
    elif widget == _button_5:
        print('Track 5')
        play(path[4])
    elif widget == _button_6:
        print('Track 6')
        play(path[5])
    elif widget == _button_7:
        print('Track 7')
        play(path[6])


if __name__ == '__main__':
    # creates music selection window
    win = Tk()
    win.title("Music Selection")


    width, height = 1000, 700
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (width / 2)
    y_coordinate = (screen_height / 2) - (height / 2)

    # adjust where it pops up
    win.geometry("%dx%d+%d+%d" %
                       (width, height, x_coordinate, y_coordinate))

    # add background
    im = tkinter.PhotoImage(file = "images/lazer_tag_bg.png")
    # im_bg = Label(win, image=im)
    # im_bg.pack()

    canvas = Canvas(win)
    canvas.pack(fill = "both", expand = True)
    canvas.create_image(0,0, image = im, anchor = "nw")
    # initialize music player
    pygame.init()

    # list all music tracks
    tracks = os.listdir('photon_tracks')
    path = ['photon_tracks/' + i for i in tracks]

    # default music selection
    pygame.mixer.music.load(path[0])
    pygame.mixer.music.play(start=300)

    top = Frame(canvas).pack(side=TOP)
    heading = Label(top, text = "Select the Music Track", font=('Times', 50)).pack(pady= 30)
    left = Frame(canvas, bg = 'black')
    left.pack(side = LEFT, padx=50)
    middle = Frame(canvas, bg = 'black')
    middle.pack(side = LEFT, padx=50)
    right = Frame(canvas, bg = 'black')
    right.pack(side=LEFT, padx=30)


    # create all buttons
    _button_1 = Button(left, text='Track 1', font=('Times', 32))
    _button_1.config(command=lambda obj=_button_1: clicked(obj))
    _button_1.bind('<<Track 1 Selected>>', clicked)
    _button_1.pack(padx = 30, pady = 30)

    _button_2 = Button(left, text='Track 2', font=('Times', 32))
    _button_2.config(command=lambda obj=_button_2: clicked(obj))
    _button_2.bind('<<Track 2 Selected>>', clicked)
    _button_2.pack(padx = 30, pady = 30)

    _button_3 = Button(left, text='Track 3', font=('Times', 32))
    _button_3.config(command=lambda obj=_button_3: clicked(obj))
    _button_3.bind('<<Track 3 Selected>>', clicked)
    _button_3.pack(padx = 30, pady = 30)

    _button_4 = Button(middle, text='Track 4', font=('Times', 32))
    _button_4.config(command=lambda obj=_button_4: clicked(obj))
    _button_4.bind('<<Track 4 Selected>>', clicked)
    _button_4.pack(padx = 30, pady = 30)

    _button_5 = Button(middle, text='Track 5', font=('Times', 32))
    _button_5.config(command=lambda obj=_button_5: clicked(obj))
    _button_5.bind('<<Track 5 Selected>>', clicked)
    _button_5.pack(padx = 30, pady = 30)

    _button_6 = Button(middle, text='Track 6', font=('Times', 32))
    _button_6.config(command=lambda obj=_button_6: clicked(obj))
    _button_6.bind('<<Track 6 Selected>>', clicked)
    _button_6.pack(padx = 30, pady = 30)

    _button_7 = Button(right, text='Track 7', font=('Times', 32))
    _button_7.config(command=lambda obj=_button_7: clicked(obj))
    _button_7.bind('<<Track 7 Selected>>', clicked)
    _button_7.pack(padx = 30, pady = 30)

    _button_8 = Button(right, text='Track 8', font=('Times', 32))
    _button_8.config(command=lambda obj=_button_8: clicked(obj))
    _button_8.bind('<<Track 8 Selected>>', clicked)
    _button_8.pack(padx = 30, pady = 30)

    p = Button(right, text='pause', font=('Times', 32), command=pause)
    p.pack(padx = 30, pady = 30)

    win.mainloop()