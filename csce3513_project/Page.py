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

        # creating empty dictionaries for things inside the window
        self.page[1]["LeftFrame"] = {}
        self.page[1]["MiddleFrame"] = {}
        self.page[1]["RightFrame"] = {}
        
        self.temp_list = ["LeftFrame", "MiddleFrame", "RightFrame"]
        # changed from lists to dictionary
        # hierarchy is list -> dictionary -> dictionary -> objects/lists of objects
        for k in self.temp_list:
                self.page[1][k]["Frame"] = Frame(self.page[0])
                print(k)
                self.page[1][k]["Frame"].pack(side=LEFT)
        self.temp_list = ["LeftFrame", "RightFrame"]
        for k in self.temp_list:
            self.page[1][k]["PlayerIDLabelList"] = [0] * 15
            self.page[1][k]["PlayerNameLabelList"] = [0] * 15
            for n in range(0,15):
                self.page[1][k]["PlayerIDLabelList"][n] = Label(self.page[1][k]["Frame"],
                                                                text="Empty Player ID")
                self.page[1][k]["PlayerIDLabelList"][n].grid(row = n, column = 0)
                self.page[1][k]["PlayerNameLabelList"][n] = Label(self.page[1][k]["Frame"],
                                                                text="Empty Player Name")           
                self.page[1][k]["PlayerNameLabelList"][n].grid(row = n, column = 1)
        
        #creation of middle Frame

        self.page[1]["MiddleFrame"]["Player Entry Button"] = Button(text="Enter New Player")
        self.page[1]["MiddleFrame"]["Player Entry Button"].pack()
        # tester loop to populate the page with buttons
        #for k in self.page[1]:
           # for n in range(1,16):
            #    self.page[1][k][n] = Button(self.page[1][k][0], text = "Button " + str(n), command = self.print(row = n,column = 0,key = k))
            #   self.page[1][k][n].grid(row = n, column = 0)
         #   for n in range(0, 15):
          #      self.page[1][k]["ButtonList"][n] = Player_Button()
           #     self.page[1][k]["ButtonList"][n].create(self.page[1][k]["Frame"], n, 0)





        self.page[0].mainloop()

