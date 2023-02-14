import inspect
class Player():
    def __init__(self, ID, NAME, SCORE, TEAM):
        self.id = ID
        self.name = NAME
        self.score = SCORE
        self.team = TEAM

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
        ##FIXED RED TEAM PLAYERS
        self.players.append(Player(1, "player 1", 100, 1))
        self.players.append(Player(2, "player 2", 20, 1))
        self.players.append(Player(3, "player 3", 40, 1))
        self.players.append(Player(4, "player 4", 10, 1))
        
        self.players.append(Player(9, "player 9", 20, 1))
        self.players.append(Player(10, "player 10", 20, 1))
        self.players.append(Player(11, "player 11", 100, 1))
        self.players.append(Player(12, "player 12", 50, 1))
        ##FIXED BLUE TEAM PLAYERS
        self.players.append(Player(1, "player 5", 10, 2))
        self.players.append(Player(6, "player 6", 80, 2))
        self.players.append(Player(7, "player 7", 50, 2))
        self.players.append(Player(8, "player 8", 50, 2))
        
        self.players.append(Player(13, "player 13", 10, 2))
        self.players.append(Player(14, "player 14", 20, 2))
        self.players.append(Player(15, "player 15", 40, 2))
        self.players.append(Player(16, "player 16", 10, 2))

#--------------------------------------------------
        self.teams = []

        self.teams.append(Team(1, "RED TEAM", 0, 0))
        self.teams.append(Team(2, "BLUE TEAM", 0, 0))
#--------------------------------------------------
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
        ##DISPLAY TEAM SCORES AND # PLAYERS
        self.DisplayTeams()

    def DisplayTeams(self):
        for team in self.teams:
            if(team.teamid == 1):
                print(team.teamname + ":")
                print("Number of Players: " + str(team.numplayers))
                print("PLAYERS: ")
                for player in self.players:
                    if(player.team == 1):
                        print(player.name)
                print("Red Team Score: " + str(team.score))

            elif(team.teamid == 2):
                print(team.teamname + ":")
                print("Number of Players: " + str(team.numplayers))
                print("PLAYERS: ")
                for player in self.players:
                    if(player.team == 2):
                        print(player.name)
                print("Blue Team Score: " + str(team.score))

scoreboard = Scoreboard()
scoreboard.build()













































