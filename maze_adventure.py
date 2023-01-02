from collections import deque
from copy import deepcopy
from typing import Deque, Dict, Generic, List, Set, Tuple, TypeVar
from stack_queue import Stack, Queue

T = TypeVar("T")
    
# U2 Project: Maze Adventure Solver
# **************************************************
# Welcome to the Maze Adventure, a labyrinth where you have to help the user find the path of shortest 
# duration to get from a start room to an end room. Implement the Maze class, which stores a maze in the form of a 
# dictionary of rooms with properties on them and finds a path through in the method solve_maze. This project
# also comes with an optional extension for the more adventurous where you need to obtain items to unlock some 
# of the rooms.  Look for "Locked Room Extension" in the comments to know what is optional. 
# 
# The solver will use a classic Breadth First Search algorithm (see OneNote) and put your Stack, Queue, Set, and Map skills to the 
# test, which offers you this chilling challenge: to find a way out, muahaha!  Of course, there's always my way...
# https://studio.code.org/projects/applab/1WKMHhvvCKtuTaZMJKRqLK09DhGdKLQb3jOTy3Cye7E

# Constants for keys to the dictionaries
ROOM_KEY = "room_name"
TIME_NEEDED_KEY = "time_needed"
TIME_TAKEN_TO_ARRIVE_HERE_KEY = "time_taken"


# Class: MazeRoom 
# **************************************************
# Stores the properties of a room in the labyrinth
# rooms_you_can_go_to (List[Dict]): A list of rooms you can get to from the current room. Each list item is a dictionary that
# contains the following key/value pairs:
#       Key (str): "room_name" (represented by constant ROOM_KEY) / Value (str): The name of the neighboring room
#       Key (str): "time_needed" (represented by constant TIME_NEEDED) / Value (int): time it takes to get to the neighboring room
#                   from the current room
# item (opt str used for the Locked Room extension only): the item that is contained in the room if any
# requires (opt str used for the Locked Room extension only): the item required to unlock the room if any
# Note: you can add whatever attributes you would like to this class.  It does not have to be limited to the parameters
class MazeRoom:
    def __init__(self, rooms_you_can_go_to: List[Dict], item: str = None, requires: str = None) -> None:
        self.rooms_you_can_go_to = rooms_you_can_go_to
        #not doing the locked extension

        #the dict contains name:time (both strings)


# Class: Maze
# ***************************************************
# Stores the map and finds the shortest duration path.  Special properties of the map:
#   -The map stores information about each room, including what rooms are connected to it and how long it
#    takes to get to that room.  Rooms can be large, so it takes more time to get to some rooms (see MazeRoom 
#    class description)
#   -You should not visit the same room more than once (unless you are doing the locked door extension)
#   -Some mazes are not solvable.  In this case, the returned stack should be None
class Maze:

    # Constructor
    # ***************************************************
    # Parameters: 
    # maze: a dictionary of all the rooms in the labyrinth and their properties. Contains key/value pairs:
    #     Key: the name of the room
    #     Value: a MazeRoom object (you should feel free to modify this object as needed)
    # start_room (str): the name of the room where you start
    # end_room(str): the name of the room you need to get to
    #
    # Note: you can add whatever attributes you would like.  It does not have to be limited to the parameters.
    def __init__(self, maze: Dict, start_room: str, end_room: str) -> None:  
        self.maze = maze
        #the maze has the room name and then the mazeroom
        #the mazeroom itself has a room name and the time required
    
        self.start_room = start_room
        self.end_room = end_room
        


    # solve_maze
    # ***************************************************
    # Finds the path of shortest duration to get from the start room to the end room.  
    # Returns a stack of dictionaries representing the shortest path, with the end room at the top of the stack and 
    # start room at the bottom. The dictionaries must include (but is not limited to) the following key/value pairs:
    #       Key (str): "room_name" (represented by constant ROOM_KEY) / Value (str): name of the room
    #       Key (str): "time_taken" (represented by constant TIME_TAKEN_TO_ARRIVE_HERE_KEY)) / 
    #                       Value (int): number of steps it took to get to this room
    # If there is no solution, this method returns None
    #
    # Important: Use deepcopy(object) to make separate copies of an object and all its inner components. Also
    # the start room should have 0 as its time taken.
    def solve_maze(self) -> Stack[Dict]:
        path = Stack()
        if self.start_room == self.end_room:
            #if the start and ending rooms are the same then theres no path
            return path
        possible_paths = Queue()
        completed_rooms = set()
        end_found = False
        #initializing


        path.push({self.start_room:TIME_TAKEN_TO_ARRIVE_HERE_KEY})
        completed_rooms.add(self.start_room)
        start_mazeroom = self.maze.get(self.start_room)
        #grab the starting mazeroom
        for x in start_mazeroom.rooms_you_can_go_to:
            new_path = deepcopy(path)
            new_path.push(x)
            #copy and add the second room 
            new_room = new_path.peek()
            if new_room.get(ROOM_KEY) == self.end_room:
                return new_path
            possible_paths.enqueue(new_path)
        

        #The stack - path - has the starting room already in (dicts{roomname:mazeroom})
        #the queue - possible paths - has the possible paths ready (stacks of dicts)
        #the set - completed rooms - has the start room only as of now (string)


        while not(end_found):
            
            #access the possible rooms you can go to, copy the original path then progress w enqueue/dequeue
            current_path = possible_paths.dequeue()
            
            
                      
           

            break


            
            

            
            
            




            


        




    # implements_locked_room_extension (optional for Locked Room Extension only)
    # ***************************************************
    # Make this return True if you implemented code for the Locked Room extension to enable the tests
    def implements_locked_room_extension(self) -> bool:
        return False
