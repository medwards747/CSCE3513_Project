from tkinter import *
from csce3513_project.Page import Page
from PIL import Image, ImageTk


def run_page():
    return Page()

class Splash:

    def __init__(self) -> None:
        # set up blank screen
        width = 427
        height = 250
        self.root = Tk()


        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (width / 2)
        y_coordinate = (screen_height / 2) - (height / 2)

        # adjust where it pops up
        self.root.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))

        # remove the heading on top
        self.root.overrideredirect(1)

        Frame(self.root, width=427, height=241, bg='black').place(x=0, y=0)


        # add logo
        im = Image.open("csce3513_project\logo.jpg")
        logo = im.resize((width, height))
        LOGO = ImageTk.PhotoImage(logo)

        # insert logo
        logo_label = Label(image=LOGO, bg = 'black')
        logo_label.place(x = 0, y = 0)

        self.root.after(3000,lambda: self.root.destroy())
        mainloop()
        run_page()










