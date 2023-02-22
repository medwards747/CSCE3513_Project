import unittest
from csce3513_project.Page import Page
from csce3513_project.game import Player, Team, Scoreboard


class TestScoreboard(unittest.TestCase):
    """Tests the Scoreboard class.

    Arguments:
        unittest -- Inherits from unittest.TestCase for unit testing.
    """

    def test_player_dictionary_import(self) -> None:
        """Tests importing the player dictionary into the Scoreboard.
        Will only display output on the console -- it does not assert anything.
        """
        test_dictionaries = [
            {
                'Green': [
                    ['1', 'Opus', 0],
                    ['3', 'BigPiccolo', 0],
                    ['5', 'testName', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0]
                ],
                'Red': [
                    ['2', 'Matt', 0],
                    ['4', 'Gomugomugomugomugomu', 0],
                    ['6', 'yo', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0],
                    ['Empty ID', 'Empty Slot', 0]
                ]
            }
        ]

        for test_dictionary in test_dictionaries:
            scoreboard = Scoreboard(test_dictionary)
            scoreboard.build()
            scoreboard.DisplayTeams()


# Run the unit tests
if __name__ == '__main__':
    unittest.main()
