from tkinter import *
import random
from csce3513_project import Music
from csce3513_project.Network import NetworkReceiver, NetworkSender


class Flash_Capable_Label(Label):

    def __init__(self, original="gray34", flash_bg="white", delay=1000, **kwrds):
        super().__init__(**kwrds)
        self.delay = delay
        self.current_flash_state = False
        self.flash_state = False
        self.original_bg = original
        self.flash_bg = flash_bg

    def flash(self):
        if self.current_flash_state:
            self.flash_state = not self.flash_state
            if self.flash_state:
                self.config(bg=self.flash_bg)
            else:
                self.config(bg=self.original_bg)
            self.after(self.delay, self.flash)
        else:
            self.flash_state = False
            self.config(bg=self.original_bg)
            self.after(self.delay, self.flash)

    def flip_state(self):
        self.current_flash_state = not self.current_flash_state
        self.flash()

    def stop_flashing(self):
        self.current_flash_state = False
        self.config(bg=self.original_bg)

    def start_flashing(self):
        self.current_flash_state = True


class Timer_Label(Label):

    def __init__(self, timer_start=391, **kwrds):
        super().__init__(**kwrds)
        self.time_remaining = timer_start
        self.minutes = self.time_remaining // 60
        self.seconds = self.time_remaining % 60
        self.config(text=str(self.seconds))

        def updateGUI():
            if self.time_remaining > 0:
                self.time_remaining -= 1
                self.minutes = self.time_remaining // 60
                self.seconds = self.time_remaining % 60
                if self.time_remaining > 360:
                    self.config(text=str(self.seconds))
                elif self.seconds < 10:
                    self.config(text=str(self.minutes) +
                                ":" + "0" + str(self.seconds))
                else:
                    self.config(text=str(self.minutes) +
                                ":" + str(self.seconds))
                if self.seconds == 0 and self.minutes == 0:
                    Player_Action.game_running = False
                elif self.seconds == 0 and self.minutes == 6:
                    Player_Action.game_running = True
                self.after(1000, updateGUI)

        updateGUI()


class Hit_Feed(Frame):
    '''Frame that holds 45 labels split into three sections, each to hold a string and be supplied a color

    Args: team_dictionary - takes the dictionary that was created in the team entry page for creation of hashtable of colors and player ids

    Notes: Hit_Feed appends hits to the end of the list_of_hits list that is then read into the list of labels in reverse order to create the falling effect.

    '''

    def __init__(self, team_dictionary, **kwrds):

        self.player_name_label_settings = {
            "padx": 2,
            "pady": 2,
            "bg": "gray34",
            "width": 28,
            "height": 1,
            "font": ("Arial", 10)}

        self.hit_label_settings = {
            "padx": 2,
            "pady": 2,
            "bg": "gray34",
            "fg": "CadetBlue1",
            "anchor": CENTER,
            "width": 7,
            "height": 1,
            "font": ("Arial", 10)}

        super().__init__(**kwrds)
        self.team_dictionary = team_dictionary
        self.list_of_hits = []
        self.left_labels = []
        self.hit_labels = []
        self.right_labels = []

        for n in range(0, 15):
            self.left_labels.append(
                Label(master=self, anchor=E, **self.player_name_label_settings))
            self.hit_labels.append(
                Label(master=self, **self.hit_label_settings))
            self.right_labels.append(
                Label(master=self, anchor=W, ** self.player_name_label_settings))
            self.left_labels[n].grid(row=n, column=0)
            self.hit_labels[n].grid(row=n, column=1)
            self.right_labels[n].grid(row=n, column=2)

    def build_hashtable(self, dictionary):
        '''Builds the hashtable for easy creation of hits when needed

        Args: dictionary: takes in the team_dictionary from init that was created on team entry page'''
        self.hashtable = {}
        for k in dictionary:
            for n in range(0, 15):
                player_id = str(dictionary[k][n][0])
                code_name = str(dictionary[k][n][1])
                self.hashtable[player_id] = [0] * 2
                self.hashtable[player_id][0] = code_name
                if k == "Green":
                    self.hashtable[player_id][1] = "limegreen"
                elif k == "Red":
                    self.hashtable[player_id][1] = "red"

    def process_hit(self, tuple):
        '''Takes in tuple of ids from network process and creates a hit using the hashtable to append appropriate values'''
        shooter_id = str(tuple[0])
        hit_id = str(tuple[1])
        hit = []
        hit.append(self.hashtable[shooter_id][0])
        hit.append(self.hashtable[shooter_id][1])
        hit.append(self.hashtable[hit_id][0])
        hit.append(self.hashtable[hit_id][1])
        self.add_hit(hit)

    def add_hit(self, hit):
        '''Adds a created hit to the list_of_hits then calls for an update to the hitfeed'''
        self.list_of_hits.append(hit)
        self.update_hitfeed()

    def add_hits(self, hits):
        """Takes a list of hits appends them to the list_of_hits then calls for an update to the hitfeed"""
        for n in range(len(hits)):
            self.list_of_hits.append(hits[n])
        self.update_hitfeed()

    def update_hitfeed(self):
        '''Reads in from the end of the list_of_hits to update the hitfeed and create a falling effect'''
        if len(self.list_of_hits) < 15:
            for n in range(len(self.list_of_hits)):
                enum = -(n+1)
                self.left_labels[n].config(
                    text=self.list_of_hits[enum][0], fg=self.list_of_hits[enum][1])
                self.hit_labels[n].config(text="hit", fg="CadetBlue1")
                self.right_labels[n].config(
                    text=self.list_of_hits[enum][2], fg=self.list_of_hits[enum][3])
        else:
            for n in range(0, 15):
                enum = -(n+1)
                self.left_labels[n].config(
                    text=self.list_of_hits[enum][0], fg=self.list_of_hits[enum][1])
                self.hit_labels[n].config(text="hit", fg="CadetBlue1")
                self.right_labels[n].config(
                    text=self.list_of_hits[enum][2], fg=self.list_of_hits[enum][3])


class Player_Action():
    game_running = False

    def __init__(self, scoreboard, music_selection) -> None:

        self.scoreboard = scoreboard
        self.music_selection = music_selection
        self.Reciever = NetworkReceiver()
        self.Sender = NetworkSender()

    def gameplay_loop(self):
        # Only process results when the timer is running
        results = self.Reciever.process_results()
        if not Player_Action.game_running:
            results = []

        if len(results) > 0:
            for result in results:
                shooter_id = result[0]
                hit_id = result[1]
                try:
                    self.page_dict["Contents"]["HitFeedFrame"].process_hit(
                        result)
                except KeyError as e:
                    print(f"ERROR: Invalid player ID received: {e}")
                    self.page_dict["Window"].after(333, self.gameplay_loop)
                    return
                self.Sender.send_hit_player(hit_id)
                self.scoreboard.hit_process(
                    hit_id=hit_id, shooter_id=shooter_id, hit_loss=0, shooter_gain=10)
                self.read_scoreboard()
                self.update_team_score()
        self.page_dict["Window"].after(333, self.gameplay_loop)

    def test_hit(self, event):
        '''Simple keypress test for functionality of hitfeed'''
        test_list = [["1", "limegreen", "2", "red"], [
            "Opus", "limegreen", "Matt", "red"], ["Matt", "red", "Opus", "limegreen"]]
        rand = random.randint(0, 2)

        self.page_dict["Contents"]["HitFeedFrame"].add_hit(test_list[rand])

    def update_team_score(self):
        green_score = int(0)
        red_score = int(0)
        for n in range(0, 15):
            green_to_add = self.page_dict["Contents"]["GreenPlayerFrame"]["ScoreLabelList"][n].cget(
                "text")
            red_to_add = self.page_dict["Contents"]["RedPlayerFrame"]["ScoreLabelList"][n].cget(
                "text")
            if green_to_add != "":
                green_score += int(green_to_add)
            if red_to_add != "":
                red_score += int(red_to_add)
        self.page_dict["Contents"]["GreenFrame"]["TeamScoreLabel"].config(
            text=str(green_score))
        self.page_dict["Contents"]["RedFrame"]["TeamScoreLabel"].config(
            text=str(red_score))

        self.page_dict["Contents"]["GreenFrame"]["Frame"].after(
            500, self.update_team_score)

    def read_scoreboard(self):
        '''Reads in the scoreboard information from the scoreboard object'''
        player_list = self.scoreboard.export_scoreboard()
        green_list = []
        red_list = []

        for n in range(0, len(player_list)):
            if player_list[n][2] == 1:
                green_list.append(player_list[n])
            elif player_list[n][2] == 2:
                red_list.append(player_list[n])
        self.read_player_data(green_list, "GreenPlayerFrame")
        self.read_player_data(red_list, "RedPlayerFrame")

    def read_player_data(self, team_list, frame):
        '''Reads a list of player information into a frame

           Args:
           team_list (list): list of lists, each sublist containing codename and score of player
           frame (tk.frame): Frame that contains the list of labels to read information into

           Notes:
           Currently hardcoded for working with Player_Action structure'''
        for n in range(0, len(team_list)):
            self.page_dict["Contents"][frame]["CNLabelList"][n].config(
                text=team_list[n][0])
            self.page_dict["Contents"][frame]["ScoreLabelList"][n].config(
                text=team_list[n][1])

    def check_flash(self):
        '''Grabs currently displayed scores on display then tests which labels should be flashing

        Notes:
        3 cases: all 4 labels should flash or only one side should flash and the other shouldn't
        Runs recursively every second which is how often the gui will update.
        '''
        outer = ["GreenFrame", "RedFrame"]
        inner = ["TeamScoreLabel", "TeamNameLabel"]
        green_score = int(
            self.page_dict["Contents"]["GreenFrame"]["TeamScoreLabel"].cget("text"))
        red_score = int(self.page_dict["Contents"]
                        ["RedFrame"]["TeamScoreLabel"].cget("text"))

        if green_score == red_score:
            for k in outer:
                for l in inner:
                    self.page_dict["Contents"][k][l].start_flashing()
        elif green_score > red_score:
            for k in outer:
                for l in inner:
                    if k == "GreenFrame":
                        self.page_dict["Contents"][k][l].start_flashing()
                    else:
                        self.page_dict["Contents"][k][l].stop_flashing()
        else:
            for k in outer:
                for l in inner:
                    if k == "RedFrame":
                        self.page_dict["Contents"][k][l].start_flashing()
                    else:
                        self.page_dict["Contents"][k][l].stop_flashing()
        self.page_dict["Window"].after(1000, self.check_flash)

    def create_play_action(self):

        # dictionary for settings labels will need {master, fg, text} in line
        self.team_label_settings = {"font": ("Arial", 25),
                                    "anchor": W,
                                    "pady": 1,
                                    "padx": 2,
                                    "bd": 5,
                                    "bg": "gray34",
                                    "width": 12}

        self.team_score_settings = {"font": ("Arial", 25),
                                    "anchor": E,
                                    "pady": 1,
                                    "padx": 2,
                                    "bd": 5,
                                    "bg": "gray34",
                                    "width": 5}

        self.player_label_settings = {
            "padx": 2,
            "pady": 2,
            "bg": "gray34",
            "anchor": W,
            "width": 32,
            "height": 1,
            "font": ("Arial", 12)}

        self.player_score_settings = {"padx": 2,
                                      "pady": 2,
                                      "bg": "gray34",
                                      "anchor": E,
                                      "width": 7,
                                      "height": 1,
                                      "font": ("Arial", 12)}

        self.timer_label_settings = {"padx":   2,
                                     "pady":   2,
                                     "bg":   "gray34",
                                     "anchor": CENTER,
                                     "bd": 5,
                                     "width": 5,
                                     "height": 1,
                                     "font": ("Arial", 25),
                                     "fg": "CadetBlue1",
                                     "timer_start": 391,
                                     "relief": RAISED
                                     }

        self.page_dict = {}
        self.page_dict["Window"] = Tk()
        self.page_dict["Contents"] = {}
        self.page_dict["Window"].config(bg="gray24")

        frame_list = ["GreenFrame",
                      "RedFrame",
                      "GreenPlayerFrame",
                      "RedPlayerFrame"]
        for k in frame_list:
            self.page_dict["Contents"][k] = {
                "Frame": Frame(self.page_dict["Window"])}

        for k in frame_list:
            self.page_dict["Contents"][k]["Frame"].config(relief=RAISED, bd=5)

        self.page_dict["Contents"]["GreenFrame"]["TeamNameLabel"] = Flash_Capable_Label(master=self.page_dict["Contents"]["GreenFrame"]["Frame"],
                                                                                        text="Green Team ",
                                                                                        fg="lime green",
                                                                                        original="gray34",
                                                                                        **self.team_label_settings)
        self.page_dict["Contents"]["RedFrame"]["TeamNameLabel"] = Flash_Capable_Label(master=self.page_dict["Contents"]["RedFrame"]["Frame"],
                                                                                      text="Red Team ", fg="red", original="gray34", **self.team_label_settings)
        self.page_dict["Contents"]["GreenFrame"]["TeamScoreLabel"] = Flash_Capable_Label(master=self.page_dict["Contents"]["GreenFrame"]["Frame"],
                                                                                         text="0", fg="lime green", original="gray34", **self.team_score_settings)
        self.page_dict["Contents"]["RedFrame"]["TeamScoreLabel"] = Flash_Capable_Label(master=self.page_dict["Contents"]["RedFrame"]["Frame"],
                                                                                       text="0", fg="red", original="gray34", **self.team_score_settings)

        self.page_dict["Contents"]["GreenPlayerFrame"]["CNLabelList"] = [
            0] * 15
        self.page_dict["Contents"]["RedPlayerFrame"]["CNLabelList"] = [0] * 15
        self.page_dict["Contents"]["GreenPlayerFrame"]["ScoreLabelList"] = [
            0] * 15
        self.page_dict["Contents"]["RedPlayerFrame"]["ScoreLabelList"] = [
            0] * 15
        temp_list = ["RedPlayerFrame", "GreenPlayerFrame"]

        for n in range(0, 15):
            self.page_dict["Contents"]["RedPlayerFrame"]["CNLabelList"][n] = Label(master=self.page_dict["Contents"]["RedPlayerFrame"]["Frame"],
                                                                                   fg="red", **self.player_label_settings)
            self.page_dict["Contents"]["RedPlayerFrame"]["CNLabelList"][n].grid(
                row=n, column=0)
            self.page_dict["Contents"]["GreenPlayerFrame"]["CNLabelList"][n] = Label(master=self.page_dict["Contents"]["GreenPlayerFrame"]["Frame"],
                                                                                     fg="lime green", **self.player_label_settings)
            self.page_dict["Contents"]["GreenPlayerFrame"]["CNLabelList"][n].grid(
                row=n, column=0)

            self.page_dict["Contents"]["RedPlayerFrame"]["ScoreLabelList"][n] = Label(master=self.page_dict["Contents"]["RedPlayerFrame"]["Frame"],
                                                                                      fg="red", **self.player_score_settings)
            self.page_dict["Contents"]["RedPlayerFrame"]["ScoreLabelList"][n].grid(
                row=n, column=1)
            self.page_dict["Contents"]["GreenPlayerFrame"]["ScoreLabelList"][n] = Label(master=self.page_dict["Contents"]["GreenPlayerFrame"]["Frame"],
                                                                                        fg="lime green", **self.player_score_settings)
            self.page_dict["Contents"]["GreenPlayerFrame"]["ScoreLabelList"][n].grid(
                row=n, column=1)

        self.page_dict["Contents"]["GreenFrame"]["Frame"].grid(row=0, column=0)
        self.page_dict["Contents"]["RedFrame"]["Frame"].grid(row=0, column=2)
        self.page_dict["Contents"]["GreenPlayerFrame"]["Frame"].grid(
            row=1, column=0)
        self.page_dict["Contents"]["RedPlayerFrame"]["Frame"].grid(
            row=1, column=2)
        temp_list = ["RedFrame", "GreenFrame"]
        for k in temp_list:
            self.page_dict["Contents"][k]["TeamNameLabel"].grid(
                row=0, column=0)
            self.page_dict["Contents"][k]["TeamScoreLabel"].grid(
                row=0, column=1)

        # creation of timer frame
        self.page_dict["Contents"]["TimerFrame"] = {}
        self.page_dict["Contents"]["TimerFrame"]["Frame"] = Frame(
            master=self.page_dict["Window"])
        self.page_dict["Contents"]["TimerFrame"]["TimerLabel"] = Timer_Label(master=self.page_dict["Contents"]["TimerFrame"]["Frame"],
                                                                             **self.timer_label_settings)
        self.page_dict["Contents"]["TimerFrame"]["Frame"].grid(row=0, column=1)
        self.page_dict["Contents"]["TimerFrame"]["TimerLabel"].grid(
            row=0, column=0)

        # creation of hitfeed
        self.page_dict["Contents"]["HitFeedFrame"] = Hit_Feed(
            team_dictionary={}, master=self.page_dict["Window"], bd=5, relief=RAISED)
        self.page_dict["Contents"]["HitFeedFrame"].grid(row=1, column=1)
        outer = ["GreenFrame", "RedFrame"]
        inner = ["TeamNameLabel", "TeamScoreLabel"]
        for k in outer:
            for l in inner:
                self.page_dict["Contents"][k][l].flash()
        self.page_dict["Window"].after(1, self.check_flash)
        self.read_scoreboard()
        self.page_dict["Contents"]["HitFeedFrame"].build_hashtable(
            self.scoreboard.dictionary)
        self.page_dict["Window"].after(1, self.gameplay_loop)
        Music.musicPlay(self.music_selection, delay=13.0)
        self.page_dict["Window"].mainloop()
