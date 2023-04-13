class Player():
    def __init__(self, player_num, id, name, team, score = 0):
        self.id = id
        self.name = name
        self.score = score
        self.team = team
        self.player_num = player_num
    
    def change_score(self, score= 100):
        self.score += score



class Team():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.num_players = 0
        self.score = 0


class Scoreboard():
    def __init__(self, dictionary):
        self.player_count = 0

        self.players = []
        self.teams = []

        self.teams.append(Team(1, "GREEN TEAM"))
        self.teams.append(Team(2, "RED TEAM"))
        self.dictionary = dictionary
        self.read_dictionary(dictionary)
        self._build()

    def add_player(self, ID, NAME, TEAM):
        print("attempting to add player")
        if not ((ID == "Empty ID") or (NAME == "Empty Slot")):
            self.player_count += 1
            self.players.append(Player(self.player_count, ID, NAME, TEAM, 0))
    
    def export_scoreboard(self):
        player_list = []
        for m in range(0,self.teams[0].num_players + self.teams[1].num_players):
            player_list.append([self.players[m].name, self.players[m].score, self.players[m].team])
        return player_list
    
    def hit_process(self, hit_id, shooter_id, hit_loss = 0, shooter_gain = 100):
        self.change_score(id = shooter_id, score = shooter_gain)
        self.change_score(id = hit_id, score = hit_loss)

    def change_score(self, id, score):
        for n in range(0,len(self.players)):
            if str(self.players[n].id) == str(id):
                self.players[n].change_score(score)

    def _build(self):
        for player in self.players:
            if (player.team == 1):
                for team in self.teams:
                    if (team.id == 1):
                        team.score += player.score
                        team.num_players += 1
            elif (player.team == 2):
                for team in self.teams:
                    if (team.id == 2):
                        team.score += player.score
                        team.num_players += 1

    def display_teams(self):
        # DISPLAY TEAM SCORES AND # PLAYERS FOR TESTING PURPOSES
        for team in self.teams:
            if (team.id == 1):
                print(team.name + ":")
                print("\tNumber of Players: " + str(team.num_players))
                print("\tPLAYERS: ")
                for player in self.players:
                    if (player.team == 1):
                        print("\t\t" + "Name: " + player.name +
                              "\t\t" + "Score: " + str(player.score))

                print("\t" + team.name + " Score: " + str(team.score))

            elif (team.id == 2):
                print(team.name + ":")
                print("\tNumber of Players: " + str(team.num_players))
                print("\tPLAYERS: ")
                for player in self.players:
                    if (player.team == 2):
                        print("\t\t" + "Name: " + player.name +
                              "\t\t" + "Score: " + str(player.score))

                print("\t" + team.name + " Score: " + str(team.score))

            print()

        print("Total Players: " + str(self.player_count))

    def read_dictionary(self, dictionary):
        # read_dictionary() will be used to read player data and add to scoreboard from page.py
        for key in dictionary:
            if (key == "Green"):
                for n in range(0, 15):
                    if dictionary[key][n][0] != "Empty ID":
                        self.add_player(
                            ID = dictionary[key][n][0], NAME = dictionary[key][n][1], TEAM = 1)
            elif (key == "Red"):
                for n in range(0, 15):
                    if dictionary[key][n][0] != "Empty ID":
                        self.add_player(
                            ID = dictionary[key][n][0], NAME = dictionary[key][n][1], TEAM = 2)

    def update_score(self, player_id, score):
        for player in self.players:
                    if (player.id == player_id):
                        num = player.score
                        player.score += score
                        if(player.score < 0):
                            player.score = 0
                        num = num-player.score
                        for team in self.teams:
                            if (player.team == team.id):
                                team.score -= num