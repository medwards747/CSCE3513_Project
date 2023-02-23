from tkinter import *


class Player_Action():
    
    def __init__(self) -> None:

        #dictionary for settings labels will need {master, fg, text} in line
        self.team_label_settings = {"font":("Arial", 25),
                                    "anchor":W, "pady":1, "padx":2,
                                    "bd":5, "bg" : "gray34", "width":12}
        self.team_score_settings = {"font":("Arial", 25),
                                    "anchor":E, "pady":1, "padx":2,
                                    "bd":5, "bg" : "gray34", "width":5}
        self.player_label_settings = {"text":"Empty Slot", "padx":2,
                                        "pady":1, "bg":"gray34",
                                        "anchor":W, "bd":0,
                                         "width":35, "height":1, "font":("Arial", 10)}
        self.player_score_settings = {"text":0, "padx":2,
                                        "pady":1, "bg":"gray34",
                                        "anchor":E, "bd":0,
                                         "width":7, "height":1, "font":("Arial", 10)}
        self.page_dict = {}
        self.page_dict["Window"] = Tk()
        self.page_dict["Contents"] = {}

        self.page_dict["Window"].config(bg = "gray24")
        
        #list of frame names
        frame_list = ["GreenFrame",
                      "RedFrame",
                      "GreenPlayerFrame",
                      "RedPlayerFrame",
                      "HitFeedFrame"]
        for k in frame_list:
            self.page_dict["Contents"][k] = {"Frame":Frame(self.page_dict["Window"])}

        

        #add reliefs to all frames with border width to make it visible
        for k in frame_list:
            self.page_dict["Contents"][k]["Frame"].config(relief=RAISED, bd = 5)

        self.page_dict["Contents"]["GreenFrame"]["TeamNameLabel"] = Label(self.page_dict["Contents"]["GreenFrame"]["Frame"],
                                                                            text="Green Team ", fg = "lime green", **self.team_label_settings)
        self.page_dict["Contents"]["RedFrame"]["TeamNameLabel"] = Label(self.page_dict["Contents"]["RedFrame"]["Frame"],
                                                                            text="Red Team ", fg="red", **self.team_label_settings)
        self.page_dict["Contents"]["GreenFrame"]["TeamScoreLabel"] = Label(self.page_dict["Contents"]["GreenFrame"]["Frame"],
                                                                            text="0", fg = "lime green", **self.team_score_settings)
        self.page_dict["Contents"]["RedFrame"]["TeamScoreLabel"] = Label(self.page_dict["Contents"]["RedFrame"]["Frame"],
                                                                            text="0", fg = "red", **self.team_score_settings)
      
        

        self.page_dict["Contents"]["GreenPlayerFrame"]["CNLabelList"] = [0] * 15
        self.page_dict["Contents"]["RedPlayerFrame"]["CNLabelList"] = [0] * 15
        self.page_dict["Contents"]["GreenPlayerFrame"]["ScoreLabelList"] = [0] * 15
        self.page_dict["Contents"]["RedPlayerFrame"]["ScoreLabelList"] = [0] * 15
        temp_list = ["RedPlayerFrame", "GreenPlayerFrame"]
        
        for n in range(0,15):
            self.page_dict["Contents"]["RedPlayerFrame"]["CNLabelList"][n]=Label(master = self.page_dict["Contents"]["RedPlayerFrame"]["Frame"],
                                                                                fg = "red",**self.player_label_settings)
            self.page_dict["Contents"]["RedPlayerFrame"]["CNLabelList"][n].grid(row=n, column = 0)
            self.page_dict["Contents"]["GreenPlayerFrame"]["CNLabelList"][n]=Label(master = self.page_dict["Contents"]["GreenPlayerFrame"]["Frame"],
                                                                                   fg = "lime green", **self.player_label_settings)
            self.page_dict["Contents"]["GreenPlayerFrame"]["CNLabelList"][n].grid(row=n, column = 0)
            
            self.page_dict["Contents"]["RedPlayerFrame"]["ScoreLabelList"][n]=Label(master = self.page_dict["Contents"]["RedPlayerFrame"]["Frame"],
                                                                                fg = "red",**self.player_score_settings)
            self.page_dict["Contents"]["RedPlayerFrame"]["ScoreLabelList"][n].grid(row=n, column = 1)
            self.page_dict["Contents"]["GreenPlayerFrame"]["ScoreLabelList"][n]=Label(master = self.page_dict["Contents"]["GreenPlayerFrame"]["Frame"],
                                                                                   fg = "lime green", **self.player_score_settings)
            self.page_dict["Contents"]["GreenPlayerFrame"]["ScoreLabelList"][n].grid(row=n, column = 1)


        

        self.page_dict["Contents"]["GreenFrame"]["Frame"].grid(row=0,column=0)
        self.page_dict["Contents"]["RedFrame"]["Frame"].grid(row=0,column=1)
        self.page_dict["Contents"]["GreenPlayerFrame"]["Frame"].grid(row=1,column=0)
        self.page_dict["Contents"]["RedPlayerFrame"]["Frame"].grid(row=1,column=1)
        self.page_dict["Contents"]["HitFeedFrame"]["Frame"].grid(row=2,column=0,columnspan=2)
        temp_list = ["RedFrame", "GreenFrame"]
        for k in temp_list:
            self.page_dict["Contents"][k]["TeamNameLabel"].grid(row = 0, column = 0)
            self.page_dict["Contents"][k]["TeamScoreLabel"].grid(row = 0, column = 1)
        self.page_dict["Window"].mainloop()


class Test_kf():

    def __init__(self) -> None:

        tk = Tk()
        frame = Frame(tk)
        frame.pack()
        label_left = Label(master=frame,
                       text = "left",
                       fg = "lime green",
                       anchor = E)
        label_middle = Label(master = frame,
                         text = " hit ",
                         fg = "black")
        label_right =   Label(master = frame,
                          text = "right",
                          fg = "red",
                          anchor = W)
        label_left.grid(row=0, column=0)
        label_middle.grid(row=0, column=1)
        label_right.grid(row=0,column=2)

        tk.mainloop()
Player_Action()
