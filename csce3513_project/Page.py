'''
Page.py
Author: Matthew Edwards
Dependencies: tkinter
Description:
Page.py is a script that uses tkinter architecture to build a player entry page for a laser tag system.
The list page contains the entire hierarchy of the GUI within a box.

Current hierarchy of page list for reference:
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
import tkinter
from tkinter import *
from functools import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from turtle import color
from csce3513_project.Database_Interface import Database_Interface
import time


def ErrorDuplicatePlayer():
    tkinter.messagebox.showerror(title = None, message= 'Already a player added')

class Page():
    # init function, what occurs as soon as Page object is created

    def updateLabelInfo(self):
        # function will read through the team_dictionary and place all the string data into the relevant slots
        frame_list = ["LeftFrame", "RightFrame"]
        for k in frame_list:
            for n in range(0, 15):
                if k == "LeftFrame":
                    self.page[1][k]["PlayerIDLabelList"][n].config(
                        text=self.team_dictionary["Green"][n][0])
                    self.page[1][k]["PlayerNameLabelList"][n].config(
                        text=self.team_dictionary["Green"][n][1])
                if k == "RightFrame":
                    self.page[1][k]["PlayerIDLabelList"][n].config(
                        text=self.team_dictionary["Red"][n][0])
                    self.page[1][k]["PlayerNameLabelList"][n].config(
                        text=self.team_dictionary["Red"][n][1])

    def updatePlayerInfo(self, team, id, name):
        # -------------------------------------------------------------------------------------------------------------
        # team should be passed in as a string, capitalized color, this will be used to reference which team to place
        # the player into
        # function takes in the team to interact with, id of player, name of player
        # tests the team dictionary for the first empty slot
        # then places the players information into the slot
        # -------------------------------------------------------------------------------------------------------------
        # typecasting of the inputs
        team_color = str(team)
        player_ID = str(id)
        player_Name = str(name)
        empty_slot_found = False
        for n in range(0, 15):
            # check if a slot has been found in the loop, and if there is an empty slot at the n slot of team_dictionary
            if self.team_dictionary[team_color][n][0] == "Empty ID" and empty_slot_found == False:
                # if a empty slot is found it saves the integer and flips the boolean
                first_Available = n
                empty_slot_found = True
        # after the above loop if a slot was found we set the relevant slot equal to provided information in
        # function call
        if empty_slot_found == True:
            self.team_dictionary[team_color][first_Available][0] = player_ID
            self.team_dictionary[team_color][first_Available][1] = player_Name
            # after changing the slot info we call the function to read team_dictionary into the label lists for gui display
            self.updateLabelInfo()
        else:
            print("No empty slot found")

    def deletePlayer(self, id):
        # -------------------------------------------------------------------------------------------------------------
        # will delete a player from the game
        # first looks for matching id in green
        # if found in green records slot and team color
        # resets slot to empty then starts a loop that moves all slots below up one and then
        # fills lasts slot with default slot info
        # thn calls for labels to be refreshed
        # -------------------------------------------------------------------------------------------------------------
        color_list = ["Green", "Red"]
        slot_number = 0
        team_color = ""
        id_found = False
        for k in color_list:
            for n in range(0, 15):
                if self.team_dictionary[k][n][0] == id:
                    slot_number = n
                    team_color = k
                    id_found = True
        if id_found == True:
            # removes the slot that is found from the player list
            # pop method is supposed to remove the selected index from the list
            self.team_dictionary[team_color].pop(slot_number)
            # adds a new empty entry at the bottom of the list
            self.team_dictionary[team_color].append([0] * 3)
            # initializes the slot info
            self.team_dictionary[team_color][14][0] = "Empty ID"
            self.team_dictionary[team_color][14][1] = "Empty Slot"
            self.team_dictionary[team_color][14][2] = 0
            self.updateLabelInfo()
        else:
            print("No ID found in any player slot")
    
    def startGame(self):
        #----------------------------------------------------------------------------------------------------
        #tests if the lobby is populated with atleast one player on each team,
        #if fail show error message
        #if pass start timer, once timer completes kill page which return team_dictionary
        #----------------------------------------------------------------------------------------------------
        if self.team_dictionary["Green"][0][0] == "Empty ID" or self.team_dictionary["Red"][0][0] == "Empty ID":
            showinfo("Error", "Both teams need atleast one player.")
        else:
            self.timer()
    
    def timer(self):
        #----------------------------------------------------------------------------------------------------
        #First tests that timer hasnt started then sets the time_remaining for the countdown timer and flips the bool
        #creates function update that will be used locally to run itself every second to update the timer
        #once the timer runs out kills the mainloop which will run the return statement
        #----------------------------------------------------------------------------------------------------
        if self.timer_started == FALSE:
            self.time_remaining = 5
            self.timer_started = TRUE
            def update():
                if self.time_remaining > 0:
                    self.time_remaining -= 1
                    self.page[1]["TopMiddleFrame"]["Label"].config(text = self.time_remaining)
                    self.page[1]["TopMiddleFrame"]["Label"].after(1000, update)
                else:
                    self.page[0].destroy()
            self.page[1]["TopMiddleFrame"]["Label"].config(text = self.time_remaining)
            self.page[1]["TopMiddleFrame"]["Label"].after(1000, update)
        if self.timer_started == TRUE:
            pass
            
    def clearAll(self):
        #----------------------------------------------------------------------------------------------------
        #Clears the team_dictionary then reinitializes all the slots
        #Runs updateLabelInfo() to read the dictionary to the labels
        #----------------------------------------------------------------------------------------------------
        if self.timer_started == FALSE:
            for n in range(0, 15):
                for k in self.team_dictionary:
                    self.team_dictionary[k].pop(0)
                    self.team_dictionary[k].append(["Empty ID",
                                                    "Empty Slot",
                                                    0])
            self.updateLabelInfo()


    def playerEntryPopup(self, team):
        #----------------------------------------------------------------------------------------------------
        #Tests that coutdown hasnt started
        #creates popup for player id to be entered
        #creates Database_Interface Object then send user input to DB through API request
        #tests if data was not recieved
        #true case-asks for player name to be entered and sends new api request to store id-name pair in DB
        #false case-checks that playerid isnt already in game then adds to the game if true
        #----------------------------------------------------------------------------------------------------
        if self.timer_started == FALSE:
            self.newID = askstring(
                team, "Enter ID to add to " + str(team) + " team:")
        # Check if ID is an integer
            try:
                self.newID = int(self.newID)
            except ValueError:
            # Display a popup message if ID is not an integer
                showinfo("Error", "ID must be an integer")
                return
            DB = Database_Interface()
            data = DB.searchID(self.newID)
            if data == False:
                self.playerNamePopup()
                if self.newPlayerName != None:  # removes cancel bug
                    self.newPlayerDictionary = {"id": self.newID,
                                            "codename": self.newPlayerName,
                                            "first_name": "None",
                                            "last_name": "None"}
                    DB.insertName(self.newPlayerDictionary)
                    self.updatePlayerInfo(team, self.newID, self.newPlayerName)
            else:
            # doesn't allow repeating id's in scoreboard
                self.rVariable = data[0]["id"]
                color_list = ["Green", "Red"]
                slot_number = 0
                team_color = ""
                id_found = False
                for k in color_list:
                    for n in range(0, 15):
                        if self.team_dictionary[k][n][0] == str(self.rVariable):
                            id_found = True
                if id_found != True:
                    self.updatePlayerInfo(team, data[0]["id"], data[0]["codename"])
                else:
                    ErrorDuplicatePlayer()

    def playerRemovalPopup(self):
        #----------------------------------------------------------------------------------------------------
        #test if timer has started, otherwise popup for id to remove from game
        #----------------------------------------------------------------------------------------------------
        if self.timer_started == FALSE:
            self.removeID = askstring(
                "Player Removal", "Enter ID to remove from game:")
            self.deletePlayer(self.removeID)

    def playerNamePopup(self):
        #----------------------------------------------------------------------------------------------------
        #popup for entry of new codename returns the entry
        #----------------------------------------------------------------------------------------------------
        self.newPlayerName = askstring(
            "New Player Name Entry", "Enter Player Code Name to match with " + str(self.newID))
        return (self.newPlayerName)

    def createTeamEntryPage(self):
        #initialize team_dictonary which acts as reference table for labels and will export to game.py
        self.team_dictionary = {}
        self.team_dictionary["Green"] = [0] * 15
        self.team_dictionary["Red"] = [0] * 15
        for n in range(0, 15):
            self.team_dictionary["Green"][n] = [0] * 3
            self.team_dictionary["Green"][n][0] = "Empty ID"
            self.team_dictionary["Green"][n][1] = "Empty Slot"
            self.team_dictionary["Green"][n][2] = 0
            self.team_dictionary["Red"][n] = [0] * 3
            self.team_dictionary["Red"][n][0] = "Empty ID"
            self.team_dictionary["Red"][n][1] = "Empty Slot"
            self.team_dictionary["Red"][n][2] = 0
        #building out the window hierarchy
        self.root = Tk()
        self.root.config(bg = "gray24")
        self.timer_started = FALSE
        self.root.resizable(width=False, height=False)
        self.page = [0]
        self.page[0] = self.root
        self.page_dictionary = {}
        self.page.append(self.page_dictionary)
        #creating empty dictionaries for things inside the window
        self.page[1]["LeftFrame"] = {}
        self.page[1]["MiddleFrame"] = {}
        self.page[1]["RightFrame"] = {}
        #temp_list is a construct for easy looping, easier to type and keep track of contents than source
        self.temp_list = ["LeftFrame", "MiddleFrame", "RightFrame"]
        self.column_num = 0
        #loop creates the entry "Frame" in each frame dictionary and adds a Frame tk object, grids them to the window
        for k in self.temp_list:
            self.page[1][k]["Frame"] = Frame(self.page[0],
                                             height=450,
                                             width=125
                                             )
            self.page[1][k]["Frame"].grid(row=1, column=self.column_num)
            self.column_num += 1
        #changing temp_list for use in loop
        self.temp_list = ["LeftFrame", "RightFrame"]
        #loop create lists in dictionary for labels of each team, total of 60 labels
        for k in self.temp_list:
            self.page[1][k]["PlayerIDLabelList"] = [0] * 15
            self.page[1][k]["PlayerNameLabelList"] = [0] * 15
            for n in range(0, 15):
                self.page[1][k]["PlayerIDLabelList"][n] = Label(self.page[1][k]["Frame"],
                                                                text="Empty ID", padx=2,
                                                                pady=1, bg="gray40",
                                                                anchor=E, bd=5,
                                                                relief=SUNKEN, width=18, height=2, font = ("Arial", 10))  # width = 10
                self.page[1][k]["PlayerIDLabelList"][n].grid(
                    row=n, column=0)
                self.page[1][k]["PlayerNameLabelList"][n] = Label(self.page[1][k]["Frame"],
                                                                  text="Empty Slot", padx=2,
                                                                  pady=1, bg="gray40",
                                                                  anchor=E, bd=5,
                                                                  relief=SUNKEN, width=35, height=2, font = ("Arial", 10))  # width = 18
                self.page[1][k]["PlayerNameLabelList"][n].grid(
                    row=n, column=1)
        # this loop sets the colors for the label lists
        for k in self.temp_list:
            for n in range(0, 15):
                if k == "LeftFrame":
                    self.page[1][k]["PlayerIDLabelList"][n].config(
                        fg="lime green")
                    self.page[1][k]["PlayerNameLabelList"][n].config(
                        fg="lime green")
                elif k == "RightFrame":
                    self.page[1][k]["PlayerIDLabelList"][n].config(fg="red")
                    self.page[1][k]["PlayerNameLabelList"][n].config(fg="red")

        # creation of top left frame
        self.page[1]["TopLeftFrame"] = {}
        self.page[1]["TopLeftFrame"]["Frame"] = Frame(self.page[0], bg="white")
        self.page[1]["TopLeftFrame"]["Frame"].grid(row=0, column=0)
        self.page[1]["TopLeftFrame"]["Green Label"] = Label(self.page[1]["TopLeftFrame"]["Frame"],
                                                            text="Green Team", fg="lime green", font=("Arial", 25),
                                                            anchor=E, pady=1, padx=2,
                                                            bd=5, bg = "gray40", relief=RAISED)
        self.page[1]["TopLeftFrame"]["Green Label"].grid(row=0, column=0)
        #creation of top middle frame
        self.page[1]["TopMiddleFrame"] = {}
        self.page[1]["TopMiddleFrame"]["Frame"] = Frame(self.page[0])
        self.page[1]["TopMiddleFrame"]["Label"] = Label(self.page[1]["TopMiddleFrame"]["Frame"],
                                                        text = "", pady = 1, padx = 2,
                                                        bd = 5, bg="gray40", fg = "CadetBlue1",font=("Arial",25),
                                                        anchor = CENTER, relief= RAISED, width =6)
        self.page[1]["TopMiddleFrame"]["Frame"].grid(row=0, column =1)
        self.page[1]["TopMiddleFrame"]["Label"].grid(row=0, column=0)
        # creation of top right frame
        self.page[1]["TopRightFrame"] = {}
        self.page[1]["TopRightFrame"]["Frame"] = Frame(
            self.page[0], bg="white")
        self.page[1]["TopRightFrame"]["Frame"].grid(row=0, column=2)
        self.page[1]["TopRightFrame"]["Red Label"] = Label(self.page[1]["TopRightFrame"]["Frame"],
                                                           text="Red Team", fg="red", font=("Arial", 25),
                                                           anchor=E, pady=1, padx=2,
                                                           bd=5, bg = "gray40", relief=RAISED)
        self.page[1]["TopRightFrame"]["Red Label"].grid(row=0, column=1)

        # creation of middle Frame
        self.page[1]["MiddleFrame"]["Game Start Button"] = Button(self.page[1]["MiddleFrame"]["Frame"],
                                                                    text="Game Start", pady=1,
                                                                          padx=2, bd=5,
                                                                          bg="gray", fg="CadetBlue1", width=25, height=2, font=("Arial", 12),
                                                                          command= self.startGame  # width = 15
                                                                          # functools used here for testing
                                                                          )
        self.page[1]["MiddleFrame"]["Player Entry Button Green"] = Button(self.page[1]["MiddleFrame"]["Frame"],
                                                                          text="Enter Green Player", pady=1,
                                                                          padx=2, bd=5,
                                                                          bg="gray", fg="CadetBlue1", width=25, height=2,  # width = 15
                                                                          # functools used here for testing
                                                                          command=partial(self.playerEntryPopup,
                                                                                          "Green"), font = ("Arial", 12))  # testing command needs replaced with function to call player entry window
        self.page[1]["MiddleFrame"]["Player Entry Button Red"] = Button(self.page[1]["MiddleFrame"]["Frame"],
                                                                        text="Enter Red Player", pady=1,
                                                                        padx=2, bd=5,
                                                                        bg="gray", fg="CadetBlue1", width=25, height=2,  # width = 15
                                                                        # functools used here for testing
                                                                        command=partial(self.playerEntryPopup,
                                                                                        "Red"), font = ("Arial", 12))  # testing command needs replaced with function to call player entry window
        self.page[1]["MiddleFrame"]["Player Deletion Button"] = Button(self.page[1]["MiddleFrame"]["Frame"],
                                                                       text="Remove Player", pady=1,
                                                                       padx=2, bd=5,
                                                                       bg="gray", fg="CadetBlue1", width=25, height=2,  # width = 15
                                                                       command=self.playerRemovalPopup, font = ("Arial", 12))  # testing command is hard coded, needs replaced with function that calls player id entry to delete
        self.page[1]["MiddleFrame"]["Clear All Button"] = Button(self.page[1]["MiddleFrame"]["Frame"],
                                                                 text="Clear All Players", pady=1,
                                                                 padx=2, bd=5,
                                                                 bg="gray", fg="CadetBlue1", width=25, height=2,  # width = 15
                                                                 command=self.clearAll, font = ("Arial", 12))
        self.page[1]["MiddleFrame"]["Game Start Button"].pack()
        self.page[1]["MiddleFrame"]["Player Entry Button Green"].pack()
        self.page[1]["MiddleFrame"]["Player Entry Button Red"].pack()
        self.page[1]["MiddleFrame"]["Player Deletion Button"].pack()
        self.page[1]["MiddleFrame"]["Clear All Button"].pack()


        self.page[0].mainloop()
        return self.team_dictionary
