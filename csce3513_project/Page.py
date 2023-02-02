from tkinter import *
from csce3513_project.Player_Button import *


class Page():
    def print(self, row, column, key):
        print("Button from the " + str(row) + " row\n the " +
              str(column) + "column\nAnd the " + str(key))
    # init function, what occurs as soon as Page object is created

    def __init__(self) -> None:
        # simple integer to keep track of what the page should be showing
        # In final version:
        # 1 -> 3 second splash screen
        # 2 -> team setup screen
        # 3 -> game running screen
        self.state = 1
        # root is the tkinter window
        self.root = Tk()
        # page will be a hierarchy of lists - outermost list contain the outermost container

        self.page = [0]
        self.page[0] = self.root
        # as well as the dictionary of all elements within the outermost layer
        self.page_dictionary = {}
        self.page.append(self.page_dictionary)

        # creating empty lists
        self.page[1]["leftFrame"] = [0] * 16
        self.page[1]["middleFrame"] = [0] * 16
        self.page[1]["rightFrame"] = [0] * 16

        # each dictionary element lead to a list of first the frame, then a list of everything within the frame
        # a different method would be for the dictionary to lead to a list which the first element would be the frame
        # then each additional element after the first would be a list containing only homogenous objects
        # a list of the buttons on that frame
        # a list of the labels on that frame, etc.
        for k in self.page[1]:
            self.page[1][k][0] = Frame(self.page[0])
            self.page[1][k][0].pack(side=LEFT)

        # tester loop to populate the page with buttons
        for k in self.page[1]:
           # for n in range(1,16):
            #    self.page[1][k][n] = Button(self.page[1][k][0], text = "Button " + str(n), command = self.print(row = n,column = 0,key = k))
            #   self.page[1][k][n].grid(row = n, column = 0)
            for n in range(1, 16):
                self.page[1][k][n] = Player_Button()
                self.page[1][k][n].create(self.page[1][k][0], n, 0)
        self.page[0].mainloop()
