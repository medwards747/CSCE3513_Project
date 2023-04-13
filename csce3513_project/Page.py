
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

import tkinter
from tkinter import *
from functools import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from turtle import color
from csce3513_project.Database_Interface import Database_Interface
from csce3513_project.Music import musicPlay

def ErrorDuplicatePlayer():
    tkinter.messagebox.showerror(title = None, message= 'Already a player added')

class Page():

    def updateLabelInfo(self):
        '''Reads through team_dictionary reference dict and places all string data into the relevant labels

           Notes:
                Should be called every time a change to team_dictionary could occur        
        '''
        frame_list = ["LeftFrame", "RightFrame"]
        for k in frame_list:
            for n in range(0, 15):
                if k == "LeftFrame":
                    self.page[1][k]["PlayerIDLabelList"][n].config(text=self.team_dictionary["Green"][n][0])
                    self.page[1][k]["PlayerNameLabelList"][n].config(text=self.team_dictionary["Green"][n][1])
                if k == "RightFrame":
                    self.page[1][k]["PlayerIDLabelList"][n].config(text=self.team_dictionary["Red"][n][0])
                    self.page[1][k]["PlayerNameLabelList"][n].config(text=self.team_dictionary["Red"][n][1])

    def updatePlayerInfo(self, team, id, name):
        ''' Places passed player id and player codename into the first empty slot of the passed team.

            Args:
                team (str): Should be either "Green" or "Red" for interface with team_dictionary
                id   (str): Player ID to add to team dictionary, will be typecasted so can be int.
                name (str): Player code name to add to team dictionary
            
            Notes:
                The reference table team_dictionary is the backend version of the gui display.
                Calls updateLabelInfo to read updated label info to the gui
        '''
        team_color = str(team)
        player_ID = str(id)
        player_Name = str(name)
        empty_slot_found = False
        for n in range(0, 15):
            if self.team_dictionary[team_color][n][0] == "Empty ID" and empty_slot_found == False:
                first_Available = n
                empty_slot_found = True
        if empty_slot_found == True:
            self.team_dictionary[team_color][first_Available] = [player_ID, player_Name]
            self.updateLabelInfo()
        else:
            print("No empty slot found")

    def deletePlayer(self, id):
        ''' Deletes a provided id from the team dictionary and updates the gui.

            Args:
                id(str): The player id to be deleted
            
            Raises:
                No errors but will print a message to console if no matching player id is found
            
            Notes:
                Adds a new empty slot to the end of the list from which a player was deleted then calls
                updatePlayerInfo
        '''
        slot_number = 0
        team_color = ""
        id_found = False
        for k in self.team_dictionary:
            for n in range(0, 15):
                if self.team_dictionary[k][n][0] == id:
                    slot_number = n
                    team_color = k
                    id_found = True
        if id_found == True:
            self.team_dictionary[team_color].pop(slot_number)
            self.team_dictionary[team_color].append(["Empty ID", "Empty Slot", 0])
            self.updateLabelInfo()
        else:
            print("No ID found in any player slot")

    
    def startGame(self):
        '''Tests if each team has atleast one player then calls timer

            Raises:
                Popup if not a player on each team
        '''

        if self.team_dictionary["Green"][0][0] == "Empty ID" or self.team_dictionary["Red"][0][0] == "Empty ID":
            showinfo("Error", "Both teams need atleast one player.")
        else:
            self.timer()
    
    def timer(self):
        '''Begins the countdown timer

           Notes:
                Flips boolean timer_started to disallow buttons to have any effect once countdown has begun.
                Once the timer hits zero the mainloop of the tk window is .destroy
        '''
        if self.timer_started == FALSE:
            self.time_remaining = 5
            self.timer_started = TRUE
            def update():
                '''Creates countdown effect with recursion'''
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

    def registerF5(self, event):
        print("f5 key pressed")
        return self.startGame()
            
    def clearAll(self):
        '''Clears all player data from the team_dictionary and fills with empty slots
           
           Notes:
                Calls updateLabelInfo to read the new "empty" dictionary to the gui.
        '''
        if self.timer_started == FALSE:
            for n in range(0, 15):
                for k in self.team_dictionary:
                    self.team_dictionary[k].pop(0)
                    self.team_dictionary[k].append(["Empty ID","Empty Slot",0])
            self.updateLabelInfo()



    def playerEntryPopup(self, team):
        '''Creates popup for entry of player id, sends input to database, adds to team_dictionary
        if a match in the team dictionary isn't found. If all checks pass calls updatePlayerInfo

        Args:
            team (str): team that the player id will attempt to be added to.

        Raises:
            ValueError: User input for player ID is not a String
        
        Notes:
            data is the dictionary returned from the SQL query from Database.
            data will be False if query returned no results.
        '''
        if self.timer_started == FALSE:
            self.newID = askstring(team, "Enter ID to add to " + str(team) + " team:")
            try:
                self.newID = int(self.newID)
            except ValueError:
                showinfo("Error", "ID must be an integer")
                return
            DB = Database_Interface()
            data = DB.searchID(self.newID)
            if data == False:
                self.playerNamePopup()
                if self.newPlayerName != None:
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
        '''Creates popup for user entry of a player id to remove, calls deleteplayer passing id'''
        if self.timer_started == FALSE:
            self.removeID = askstring(
                "Player Removal", "Enter ID to remove from game:")
            self.deletePlayer(self.removeID)

    def playerNamePopup(self):
        '''Creates popup for user entry of a player code name
        
            Returns:
                newPlayerName(str): user input intended for addition to database and gui.
        '''
        self.newPlayerName = askstring(
            "New Player Name Entry", "Enter Player Code Name to match with " + str(self.newID))
        return (self.newPlayerName)

    def runMusicWin(self):
        ''' If music selection button is pressed Music Selection Window will run'''

        return (musicPlay())


    def createTeamEntryPage(self):
        '''Creates team_dictionary for reference, page, a dictionary containing all tk elements

            Returns:
                team_dictionary(dict): dictionary containing all participating player ids and codenames

            Notes: 
                Initializes team_dictionary with all "empty" data
                As much as possible tk gui args are in dictionaries for easy editing
        '''
        #initialize team_dictonary which acts as reference table for labels and will export to game.py
        self.team_dictionary = {}
        self.team_dictionary["Green"] = [0] * 15
        self.team_dictionary["Red"] = [0] * 15
        for n in range(0, 15):
            self.team_dictionary["Green"][n] = ["Empty ID", "Empty Slot", 0]
            self.team_dictionary["Red"][n]   = ["Empty ID", "Empty Slot", 0]

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
            self.page[1][k]["Frame"] = Frame(self.page[0],height=450,width=125)
            self.page[1][k]["Frame"].grid(row=1, column=self.column_num)
            self.column_num += 1

        #changing temp_list for use in loop
        self.temp_list = ["LeftFrame", "RightFrame"]

        #loop create lists in dictionary for labels of each team, total of 60 labels
        self.player_label_dictionary = {'padx':2,'pady':1,'bg':"gray40",'anchor':E,'bd':5,'relief':SUNKEN,'height':2,'font':("Arial", 10)}
        for k in self.temp_list:
            self.page[1][k]["PlayerIDLabelList"] = [0] * 15
            self.page[1][k]["PlayerNameLabelList"] = [0] * 15
            for n in range(0, 15):
                self.page[1][k]["PlayerIDLabelList"][n] = Label(self.page[1][k]["Frame"],text="Empty ID",width=18,
                                                                **self.player_label_dictionary)  
                self.page[1][k]["PlayerIDLabelList"][n].grid(row=n, column=0)
                self.page[1][k]["PlayerNameLabelList"][n] = Label(self.page[1][k]["Frame"],text="Empty Slot",width=35,
                                                                   **self.player_label_dictionary)
                self.page[1][k]["PlayerNameLabelList"][n].grid(row=n, column=1)

        # this loop sets the colors for the label lists
        for k in self.temp_list:
            for n in range(0, 15):
                if k == "LeftFrame":
                    self.page[1][k]["PlayerIDLabelList"][n].config(fg="lime green")
                    self.page[1][k]["PlayerNameLabelList"][n].config(fg="lime green")
                elif k == "RightFrame":
                    self.page[1][k]["PlayerIDLabelList"][n].config(fg="red")
                    self.page[1][k]["PlayerNameLabelList"][n].config(fg="red")

        self.shared_top_frame_dictionary = {'font':("Arial", 25),'anchor':CENTER,'pady':1,'padx':2,'bd':5,'bg':"gray40",'relief':RAISED}
        # creation of top left frame

        self.page[1]["TopLeftFrame"] = {}
        self.page[1]["TopLeftFrame"]["Frame"] = Frame(self.page[0], bg="white")
        self.page[1]["TopLeftFrame"]["Frame"].grid(row=0, column=0)
        self.page[1]["TopLeftFrame"]["Green Label"] = Label(self.page[1]["TopLeftFrame"]["Frame"],text="Green Team",fg="lime green",width=12,
                                                            **self.shared_top_frame_dictionary)
        self.page[1]["TopLeftFrame"]["Green Label"].grid(row=0, column=0)

        #creation of top middle frame

        self.page[1]["TopMiddleFrame"] = {}
        self.page[1]["TopMiddleFrame"]["Frame"] = Frame(self.page[0])
        self.page[1]["TopMiddleFrame"]["Label"] = Label(self.page[1]["TopMiddleFrame"]["Frame"],text = "",fg = "CadetBlue1",width =6,
                                                        **self.shared_top_frame_dictionary)
        self.page[1]["TopMiddleFrame"]["Frame"].grid(row=0, column =1)
        self.page[1]["TopMiddleFrame"]["Label"].grid(row=0, column=0)

        # creation of top right frame

        self.page[1]["TopRightFrame"] = {}
        self.page[1]["TopRightFrame"]["Frame"] = Frame(
            self.page[0], bg="white")
        self.page[1]["TopRightFrame"]["Frame"].grid(row=0, column=2)
        self.page[1]["TopRightFrame"]["Red Label"] = Label(self.page[1]["TopRightFrame"]["Frame"],text="Red Team", fg="red", width=12,
                                                           **self.shared_top_frame_dictionary)
        self.page[1]["TopRightFrame"]["Red Label"].grid(row=0, column=1)

        # creation of middle Frame
        # mfargs is a dictionary of lists containing information about each button to create
        self.mfargs =   [["Game Start Button",{"text":"Game Start", "command":self.startGame}],
                        ["Player Entry Button Green",{"text":"Enter Green Player","command":partial(self.playerEntryPopup,"Green")}],
                        ["Player Entry Button Red",{"text":"Enter Red Player","command":partial(self.playerEntryPopup, "Red")}],
                        ["Player Deletion Button",{"text":"Remove Player","command":self.playerRemovalPopup}],
                        ["Clear All Button",{"text":"Clear All Players","command":self.clearAll}],
                        ["Music Selection Button",{"text":"Change Music","command": self.runMusicWin}]]
        self.button_options_dictionary = {"pady":1,"padx":2, 'bd':5,'bg':"gray40", 'fg':"CadetBlue1", 'width':25, 'height':2,'font' : ("Arial", 12)}
        #loops through each entry of mfargs and creates then packs the button
        for n in range(0,6):
            self.page[1]["MiddleFrame"][self.mfargs[n][0]]=Button(self.page[1]["MiddleFrame"]["Frame"],**self.mfargs[n][1],**self.button_options_dictionary)
            self.page[1]["MiddleFrame"][self.mfargs[n][0]].pack()

        # if f5 key is registered, then game starts
        self.page[0].bind("<F5>", self.registerF5)

        self.page[0].mainloop()
        return self.team_dictionary
