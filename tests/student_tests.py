from unittest import TestCase
from maze_adventure import MazeRoom, ROOM_KEY, TIME_NEEDED_KEY, Maze, TIME_TAKEN_TO_ARRIVE_HERE_KEY

class maze_adventure_student_tests(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_student_case(self):
        map = {
            "A" : MazeRoom([{ROOM_KEY:"B", TIME_NEEDED_KEY:1}, {ROOM_KEY:"D", TIME_NEEDED_KEY: 1}]),
            "B" : MazeRoom([{ROOM_KEY:"C", TIME_NEEDED_KEY:1}]),
            "C" : MazeRoom([{ROOM_KEY:"A", TIME_NEEDED_KEY:1}, {ROOM_KEY:"D", TIME_NEEDED_KEY:2}]),
            "D" : MazeRoom([])
        }

        maze = Maze(map, "A", "A")
        answer = maze.solve_maze()
        self.assertEqual(answer, None)

        maze = Maze(map, "B", "D")
        answer = maze.solve_maze()
        round1 = answer.pop()
        self.assertEqual(round1[ROOM_KEY], "D")
        self.assertEqual(round1[TIME_TAKEN_TO_ARRIVE_HERE_KEY], 2)
        round2 = answer.pop()
        self.assertEqual(round2[ROOM_KEY], "C")
        self.assertEqual(round2[TIME_TAKEN_TO_ARRIVE_HERE_KEY], 1)
        round3 = answer.pop()
        self.assertEqual(round3[ROOM_KEY], "B")
        self.assertEqual(round3[TIME_TAKEN_TO_ARRIVE_HERE_KEY], 0)
