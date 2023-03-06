import inspect


class Player():
    def __init__(self, PLAYERNUM, ID, NAME, SCORE, TEAM):
        self.id = ID
        self.name = NAME
        self.score = SCORE
        self.team = TEAM
        self.playernum = PLAYERNUM


class Team():
    def __init__(self, TEAMID, TEAMNAME, NUMPLAYERS, SCORE):
        self.teamid = TEAMID
        self.teamname = TEAMNAME
        self.numplayers = NUMPLAYERS
        self.score = SCORE


class Scoreboard():
    def __init__(self, dictionary):
        self.playerCount = 0

        self.players = []
        self.teams = []

        self.teams.append(Team(1, "RED TEAM", 0, 0))
        self.teams.append(Team(2, "BLUE TEAM", 0, 0))

        self.ReadDictionary(dictionary)
        self.build()

    def addPlayer(self, ID, NAME, TEAM):
        if ((ID == "Empty ID") or (NAME == "Empty Slot")):
            pass
        else:
            self.playerCount += 1
            self.players.append(Player(self.playerCount, ID, NAME, 0, TEAM))

    def build(self):
        for player in self.players:
            if (player.team == 1):
                for team in self.teams:
                    if (team.teamid == 1):
                        team.score += player.score
                        team.numplayers += 1
            elif (player.team == 2):
                for team in self.teams:
                    if (team.teamid == 2):
                        team.score += player.score
                        team.numplayers += 1

# DISPLAY TEAM SCORES AND # PLAYERS FOR TESTING PURPOSES
    def DisplayTeams(self):
        for team in self.teams:
            if (team.teamid == 1):
                print(team.teamname + ":")
                print("\tNumber of Players: " + str(team.numplayers))
                print("\tPLAYERS: ")
                for player in self.players:
                    if (player.team == 1):
                        print("\t\t" + player.name)
                print("\t" + team.teamname + " Score: " + str(team.score))

            elif (team.teamid == 2):
                print(team.teamname + ":")
                print("\tNumber of Players: " + str(team.numplayers))
                print("\tPLAYERS: ")
                for player in self.players:
                    if (player.team == 2):
                        print("\t\t" + player.name)
                print("\t" + team.teamname + " Score: " + str(team.score))

            print()

        print("Total Players: " + str(self.playerCount))

# ReadDictionary() will be used to read player data and add to scoreboard from page.py
    def ReadDictionary(self, dictionary):
        for green in dictionary:
            if (green == "Green"):
                for n in range(0, 15):
                    if (dictionary[green][n][0] == "Empty ID"):
                        pass
                    else:
                        self.addPlayer(
                            dictionary[green][n][0], dictionary[green][n][1], 1)
        for red in dictionary:
            if (red == "Red"):
                for n in range(0, 15):
                    if (dictionary[red][n][0] == "Empty ID"):
                        pass
                    else:
                        self.addPlayer(
                            dictionary[red][n][0], dictionary[red][n][1], 2)
