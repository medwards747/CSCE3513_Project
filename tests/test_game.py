import random
import unittest
from csce3513_project.game import Scoreboard


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
            scoreboard.display_teams()

    def test_player_update_score(self) -> None:
        """Tests updating the player score.
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
            scoreboard.display_teams()
            for _ in range(5):
                for user in test_dictionary['Green']:
                    if user[1] != 'Empty Slot':
                        user_id = user[0]

                        # Add a random number of points to the user
                        score_to_add = random.randint(-10, 10)
                        print("Score Added: " + str(score_to_add))
                        scoreboard.update_score(user_id, score_to_add)

                for user in test_dictionary['Red']:
                    if user[1] != 'Empty Slot':
                        user_id = user[0]
                        score_to_add = random.randint(-10, 10)
                        print("Score Added: " + str(score_to_add))
                        scoreboard.update_score(user_id, score_to_add)

                # Print the scoreboard every iteration
                scoreboard.display_teams()


# Run the unit tests
if __name__ == '__main__':
    unittest.main()
