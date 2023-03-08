class Player():
    def __init__(self, player_num, id, name, score, team):
        self.id = id
        self.name = name
        self.score = score
        self.team = team
        self.player_num = player_num


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

        self.read_dictionary(dictionary)
        self._build()

    def add_player(self, ID, NAME, TEAM):
        if not ((ID == "Empty ID") or (NAME == "Empty Slot")):
            self.player_count += 1
            self.players.append(Player(self.player_count, ID, NAME, 0, TEAM))

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
        for green in dictionary:
            if (green == "Green"):
                for n in range(0, 15):
                    if dictionary[green][n][0] != "Empty ID":
                        self.add_player(
                            dictionary[green][n][0], dictionary[green][n][1], 1)
        for red in dictionary:
            if (red == "Red"):
                for n in range(0, 15):
                    if dictionary[red][n][0] != "Empty ID":
                        self.add_player(
                            dictionary[red][n][0], dictionary[red][n][1], 2)

    def update_score(self, player_id, score):
        for player in self.players:
                    if (player.id == player_id):
                        player.score += score
                        if(player.score < 0):
                            player.score = 0
                        for team in self.teams:
                            if (player.team == team.id):
                                team.score += score
                                if(team.score < 0):
                                    team.score = 0