'''
Player Button is an attempt at creating a button that can keep track of its own state for different graphics to be displayed on it
'''


from tkinter import *


class Player_Button:

    def __init__(self) -> None:
        self.state = 1

    def create(self, master, num, num2):
        self.b = Button(master, text = "1", command = self.interact)
        self.button_id = num
        self.b.grid(row = num, column = num2)

    def change_state(self):
        #change state is the non interaction version of interact
        #useful for wen you want to change state of button without interacting with players
        #change state will change button from being grayed out
        #state 1 will be default state - grayed out - no interaction - waiting for buttons above to change in order to become interactable
        #state 2 will be add player state
        #state 3 will be remove player state
        if self.state == 1:
            self.state = 2
            self.b.config(text = "2")
        elif self.state == 2:
            self.b.config(text = "3")
            self.state = 3
        elif self.state == 3:
            self.b.config(text = "1")
            self.state = 1
        #optimally this should interact with the player dictionary to determine which state it should be in
        #player dictionary currently not created

    def interact(self):
        #what happens when end user clicks on a button
        #changes state then communicates around to inact change
        self.change_state()
        print("button " + str(self.button_id) + "'s state is " + str(self.state))

'''
#---------testing-----------

root = Tk()
frame = Frame(root)
frame.pack()
button_dictionary = {}

for n in range(0, 10):
    button_dictionary[n] = Player_Button()
    button_dictionary[n].create(master = frame, num = n)


root.mainloop()
'''