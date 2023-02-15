#!/usr/bin/env python3

# Run the program
if __name__ == '__main__':
    from csce3513_project import Page, Splash, game

    Splash.Splash()
    gui = Page.Page()
    player_data = gui.createTeamEntryPage()
    scoreboard = game.Scoreboard(player_data)
    ##Use build for testing ReadDictionary() in game.py
    scoreboard.build()