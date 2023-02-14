#!/usr/bin/env python3

# Run the program
if __name__ == '__main__':
	from csce3513_project import Page
	from csce3513_project import Splash

	Splash.Splash()
	gui = Page.Page()
	gui.createTeamEntryPage()
