from tkinter import *

root = Tk()

frame = Frame(root, height=500, width = 250)
frame.pack()
label = Label(frame,
                bg = "black",
                text = "hello",
                fg = "white",
                bd = 5)
label.pack()
root.mainloop()