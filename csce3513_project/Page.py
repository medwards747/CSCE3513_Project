'''
Page.py
Author: Matthew Edwards
Dependencies: tkinter
Description:
Page.py is a script that uses tkinter architecture to build a player entry page for a laser tag system.
The list page contains the entire hierarchy of the GUI within a box.

Current hierarchy of page list:
[] outermost list
    0 - contains the root tk window
    1 - contains a dictionary
[]  {}
    "LeftFrame" - contains a dictionary
    "RightFrame" - contains a dictionary
    "MiddleFrame" - contains a dictionary
[]  {}  {}
    the dictionaries at this level contain either the objects themselves or lists of objects within the above container
[]  {}  {}  []
    the lists at this level contain labels


'''




from tkinter import *
#functools dependency is for testing
from functools import *


class Page():
        # init function, what occurs as soon as Page object is created
     
    def updateLabelInfo(self):
        #function will read through the team_dictionary and place all the string data into the relevant slots
        frame_list = ["LeftFrame", "RightFrame"]
        for k in frame_list:
            for n in range(0,15):
                if k == "LeftFrame":
                    self.page[1][k]["PlayerIDLabelList"][n].config(text = self.team_dictionary["Green"][n][0])
                    self.page[1][k]["PlayerNameLabelList"][n].config(text = self.team_dictionary["Green"][n][1])
                if k == "RightFrame":
                    self.page[1][k]["PlayerIDLabelList"][n].config(text = self.team_dictionary["Red"][n][0])
                    self.page[1][k]["PlayerNameLabelList"][n].config(text = self.team_dictionary["Red"][n][1])

    def updatePlayerInfo(self, team, id, name):
        #-------------------------------------------------------------------------------------------------------------
        #team should be passed in as a string, capitalized color, this will be used to reference which team to place
        #the player into
        #function takes in the team to interact with, id of player, name of player
        #tests the team dictionary for the first empty slot
        #then places the players information into the slot
        #-------------------------------------------------------------------------------------------------------------
        #typecasting of the inputs
        team_color = str(team)
        player_ID = str(id)
        player_Name = str(name)
        empty_slot_found = False
        for n in range(0,15):
            #check if a slot has been found in the loop, and if there is an empty slot at the n slot of team_dictionary
            if self.team_dictionary[team_color][n][0] == "Empty ID" and empty_slot_found == False:
                #if a empty slot is found it saves the integer and flips the boolean
                first_Available = n
                empty_slot_found = True
        #after the above loop if a slot was found we set the relevant slot equal to provided information in
        #function call
        if empty_slot_found == True:
            self.team_dictionary[team_color][first_Available][0] = player_ID
            self.team_dictionary[team_color][first_Available][1] = player_Name
            #after changing the slot info we call the function to read team_dictionary into the label lists for gui display
            self.updateLabelInfo()
        else:
            print("No empty slot found")

    def deletePlayer(self, id):
        #-------------------------------------------------------------------------------------------------------------
        #will delete a player from the game
        #first looks for matching id in green
        #if found in green records slot and team color
        # resets slot to empty then starts a loop that moves all slots below up one and then 
        #fills lasts slot with default slot info
        #thn calls for labels to be refreshed
        #-------------------------------------------------------------------------------------------------------------
        color_list = ["Green", "Red"]
        slot_number = 0
        team_color = ""
        id_found = False
        for k in color_list:
            for n in range(0,15):
                if self.team_dictionary[k][n][0] == id:
                    slot_number = n
                    team_color = k
                    id_found = True
        if id_found == True:
            #removes the slot that is found from the player list
            #pop method is supposed to remove the selected index from the list
            self.team_dictionary[team_color].pop(slot_number)
            #adds a new empty entry at the bottom of the list
            self.team_dictionary[team_color].append([0] * 3)
            #initializes the slot info
            self.team_dictionary[team_color][14][0] = "Empty ID"
            self.team_dictionary[team_color][14][1] = "Empty Slot"
            self.team_dictionary[team_color][14][2] = 0
            self.updateLabelInfo()
        else:
            print("No ID found in any player slot")
    
    

    def __init__(self) -> None:
        # root is the tkinter window
        self.root = Tk()
        # page will be a hierarchy of lists - outermost list contain the outermost container
        
        #-------------------------------------------------------------------------------------------------------------
        #team_dictionary is what the gui will reference to fill the label lists
        #team_dictionary ->
        #team color ->
        #list of player [id, name, score]
        #initializing the dictionary laid out above
        #-------------------------------------------------------------------------------------------------------------
        self.team_dictionary = {}
        self.team_dictionary["Green"] = [0] * 15
        self.team_dictionary["Red"] = [0] * 15
        for n in range(0,15):
            self.team_dictionary["Green"][n] = [0] * 3
            self.team_dictionary["Green"][n][0] = "Empty ID"
            self.team_dictionary["Green"][n][1] = "Empty Slot"
            self.team_dictionary["Green"][n][2] = 0
            self.team_dictionary["Red"][n] = [0] * 3
            self.team_dictionary["Red"][n][0] = "Empty ID"
            self.team_dictionary["Red"][n][1] = "Empty Slot"
            self.team_dictionary["Red"][n][2] = 0

        #-------------------------------------------------------------------------------------------------------------
        self.page = [0]
        self.page[0] = self.root
        self.page[0].geometry("850x600")
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
                self.page[1][k]["Frame"].pack(side=LEFT)
                self.temp_num += 1
        self.temp_list = ["LeftFrame", "RightFrame"]

        for k in self.temp_list:
            self.page[1][k]["PlayerIDLabelList"] = [0] * 15
            self.page[1][k]["PlayerNameLabelList"] = [0] * 15
            for n in range(0,15):
                self.page[1][k]["PlayerIDLabelList"][n] = Label(self.page[1][k]["Frame"],
                                                                text="Empty ID", padx=2,
                                                                pady=1,bg = "gray",
                                                                anchor=E,bd = 5,
                                                                relief = SUNKEN,width = 10)
                self.page[1][k]["PlayerIDLabelList"][n].grid(row = n, column = 0)
                self.page[1][k]["PlayerNameLabelList"][n] = Label(self.page[1][k]["Frame"],
                                                                text="Empty Slot",padx = 2,
                                                                pady=1,bg = "gray",
                                                                anchor = E,bd = 5,
                                                                relief = SUNKEN,width = 18)           
                self.page[1][k]["PlayerNameLabelList"][n].grid(row = n, column = 1)
        
        #creation of middle Frame

        self.page[1]["MiddleFrame"]["Player Entry Button"] = Button(self.page[1]["MiddleFrame"]["Frame"],
                                                                    text="Enter New Player", pady = 1,
                                                                    padx = 2, bd = 5,
                                                                    bg = "gray", fg = "black", width = 15,
                                                                    #functools used here for testing
                                                                    command = partial(self.updatePlayerInfo,
                                                                                      "Green",
                                                                                      "Some",
                                                                                      "Thing")) #testing command needs replaced with function to call player entry window
        self.page[1]["MiddleFrame"]["Player Deletion Button"] = Button(self.page[1]["MiddleFrame"]["Frame"],
                                                                    text = "Remove Player", pady = 1,
                                                                    padx = 2, bd = 5,
                                                                    bg = "gray", fg = "black", width = 15,
                                                                    command = partial(self.deletePlayer,
                                                                    "Some")) #testing command is hard coded, needs replaced with function that calls player id entry to delete
        self.page[1]["MiddleFrame"]["Player Entry Button"].pack()
        self.page[1]["MiddleFrame"]["Player Deletion Button"].pack()

        self.page[0].mainloop()