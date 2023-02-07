from tkinter import *
from Page import Page
from PIL import Image, ImageTk



# set up blank screen
splash_root = Tk()

width = 427
height = 250
screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (width / 2)
y_coordinate = (screen_height / 2) - (height / 2)

# adjust where it pops up
splash_root.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))

# remove the heading on top
splash_root.overrideredirect(1)



a = '#000000'
Frame(splash_root, width=427, height=241, bg='black').place(x=0, y=0)


# add logo
im = Image.open(r"C:\Users\14794\Documents\Software_Engineering\GUI\logo.jpg")
logo = im.resize((width, height))
LOGO = ImageTk.PhotoImage(logo)

# insert logo
logo_label = Label(image=LOGO)
logo_label.place(x = 0, y = 0)


def run_page():
    splash_root.destroy()
    Page()



splash_root.after(3000,run_page)

mainloop()
