from tkinter import *
from csce3513_project.Player_Button import *


class Page():
    # init function, what occurs as soon as Page object is created

    def __init__(self) -> None:
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
        self.color_list = ["green", "black", "red"]
        self.temp_num = 0
        for k in self.temp_list:

                self.page[1][k]["Frame"] = Frame(self.page[0],
                                                bg=self.color_list[self.temp_num],
                                                height = 450,
                                                width = 125)
                print(k)
                print(self.color_list[self.temp_num])
                self.page[1][k]["Frame"].pack(side=LEFT)
                self.temp_num += 1
        self.temp_list = ["LeftFrame", "RightFrame"]

        for k in self.temp_list:
            self.page[1][k]["PlayerIDLabelList"] = [0] * 15
            self.page[1][k]["PlayerNameLabelList"] = [0] * 15
            for n in range(0,15):
                self.page[1][k]["PlayerIDLabelList"][n] = Label(self.page[1][k]["Frame"],
                                                                text="Empty Player ID", padx=2,
                                                                pady=1,bg = "gray",
                                                                anchor=E,bd = 5,
                                                                relief = SUNKEN,width = 10)
                self.page[1][k]["PlayerIDLabelList"][n].grid(row = n, column = 0)
                self.page[1][k]["PlayerNameLabelList"][n] = Label(self.page[1][k]["Frame"],
                                                                text="Empty Player Name",padx = 2,
                                                                pady=1,bg = "gray",
                                                                anchor = E,bd = 5,
                                                                relief = SUNKEN,width = 18)           
                self.page[1][k]["PlayerNameLabelList"][n].grid(row = n, column = 1)
        
        #creation of middle Frame

        self.page[1]["MiddleFrame"]["Player Entry Button"] = Button(self.page[1]["MiddleFrame"]["Frame"],
                                                                    text="Enter New Player", pady = 1,
                                                                    padx = 2, bd = 5,
                                                                    bg = "gray", fg = "black", width = 15)
        self.page[1]["MiddleFrame"]["Player Entry Button"].pack()

        self.page[0].mainloop()

# updates the labels to clear them/ or update them
'''
    def updateLabels(self):
        temp_list = ["LeftFrame", "RightFrame"]
        for k in temp_list:
            for n in range(0,15):
                self.page[1][k]["PlayerIDLabelList"][n].config(text = )
                self.page[1][k]["PlayerNameLabelList"][n].config(text =)

list of functions that are needed
1. update labels - a function that will update the labels across the window to the correct ids and names
2. player entry - a function that asks for input of player id
                    if the player id is not found in the database then ask for a new name and store it in the database and update the lists
3. update team label list - grabs from the player list to get an updated in order list to transplant to the label widgets
4. add player green - takes id and name and adds to first empty slot of list of green players
5. add player red - takes id and name and adds to first empty slot of list of red players
'''