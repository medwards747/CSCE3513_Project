import inspect

class Player():
    def __init__(self, PLAYERNUM, ID, NAME, SCORE, TEAM):
        self.id = ID
        self.name = NAME
        self.score = SCORE
        self.team = TEAM
        self.playernum = PLAYERNUM
        ##def update(self):
class Team():
    def __init__(self, TEAMID, TEAMNAME, NUMPLAYERS, SCORE):
        self.teamid = TEAMID
        self.teamname = TEAMNAME
        self.numplayers = NUMPLAYERS
        self.score = SCORE

class Scoreboard():
    def __init__(self):
        self.playerCount = 0
#--------------------------------------------------
        self.players = []
        ##Test cases for adding players from dictionary using addPlayer()
        self.addPlayer(0, "Goku", 1)
        self.addPlayer(3, "BigPiccolo", 2)
        self.addPlayer(3445, "Krillin", 1)
        self.addPlayer(1151, "Vegeta", 2)
        self.addPlayer("Empty ID", "peepee", 1)
        self.addPlayer(6969, "Empty Slot", 2)
#--------------------------------------------------
        self.teams = []

        self.teams.append(Team(1, "RED TEAM", 0, 0))
        self.teams.append(Team(2, "BLUE TEAM", 0, 0))
#--------------------------------------------------

    def addPlayer(self, ID, NAME, TEAM):
        if((ID == "Empty ID")or(NAME == "Empty Slot")):
            pass
        else:
            self.playerCount += 1
            self.players.append(Player(self.playerCount, ID, NAME, 0, TEAM))

    def build(self):
        for player in self.players:
           if(player.team == 1):
                for team in self.teams:
                    if(team.teamid == 1):
                        team.score += player.score
                        team.numplayers += 1
           elif(player.team == 2):
                for team in self.teams:
                    if(team.teamid == 2):
                        team.score += player.score
                        team.numplayers += 1
        self.DisplayTeams()
        print("Total Players: " + str(self.playerCount))

##DISPLAY TEAM SCORES AND # PLAYERS FOR TESTING PURPOSES
    def DisplayTeams(self):
        for team in self.teams:
            if(team.teamid == 1):
                print(team.teamname + ":")
                print("Number of Players: " + str(team.numplayers))
                print("PLAYERS: ")
                for player in self.players:
                    if(player.team == 1):
                        print(player.name)
                print("Green Team Score: " + str(team.score))

            elif(team.teamid == 2):
                print(team.teamname + ":")
                print("Number of Players: " + str(team.numplayers))
                print("PLAYERS: ")
                for player in self.players:
                    if(player.team == 2):
                        print(player.name)
                print("Red Team Score: " + str(team.score))

    ##def SortTeamScore(self):

##ReadDictionary() will be used to read player data and add to scoreboard from page.py
    def ReadDictionary(self, dictionary):
        for green in dictionary:
            if(green == "Green"):
                for n in dictionary[green]:
                    if(dictionary[green][n][0] == "Empty ID"):
                        pass
                    else:
                        self.addPlayer(dictionary[green][n][0], dictionary[green][n][1], 1)
        for red in dictionary:
            if(red == "Red"):
                for n in dictionary[red]:
                    if(dictionary[red][n][0] == "Empty ID"):
                        pass
                    else:
                        self.addPlayer(dictionary[red][n][0], dictionary[red][n][1], 2)

scoreboard = Scoreboard()
scoreboard.build()













































