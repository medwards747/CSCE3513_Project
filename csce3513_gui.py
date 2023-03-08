#!/usr/bin/env python3

# Run the program
if __name__ == '__main__':
    from csce3513_project import Page, Splash, game, Player_Action

    Splash.Splash()
    gui = Page.Page()
    player_data = gui.createTeamEntryPage()
    scoreboard = game.Scoreboard(player_data)
    gui = Player_Action.Player_Action()
    gui.create_play_action()
