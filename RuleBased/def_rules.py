from def_solver import *
from def_maze_entry_point import maze





class Rule:

    def __init__(self, condition, action):
        self.condition = condition
        self.action = action

    def matches(self, state):
        return self.condition(state)

    def execute(self, state):
        return self.action(state)
    
  

def can_move_right(state):
    x, y, _maze = state
    return y + 1 < len(_maze[0]) and _maze[x][y + 1] == 0

    
def move_right(state):
    x, y, maze = state
    return (x, y+1, maze)
    
def can_move_left(state):
    x, y, maze = state
    return y - 1 >= 0 and maze[x][y-1] == 0
    
def move_left(state):
    x, y, maze = state
    return (x, y-1, maze)

def can_move_up(state):
    x, y, maze = state
    return x - 1 >= 0 and maze[x-1][y] == 0

def move_up(state):
    x, y, maze = state
    return (x-1, y, maze)

def can_move_down(state):
    x, y, maze = state
    return x + 1 < len(maze) and maze[x+1][y] == 0

def move_down(state):
    x, y, maze = state
    return (x+1, y, maze)

def is_visited(self, state):
    """Check if the current position (x, y) is in the set of visited cells."""
    x, y, _ = state  # Extract position (ignore maze from state)
    return (x, y) in self.visitedCellsAndRuleUsed

def mark_visited(self, state):
    """mark the given state (position) as visited."""
    x, y, _ = state  # Extract position (ignore maze from state)
    self.visited_cells.add((x, y))  # Add position to visited_cells set

def is_goal(state, goal):
    x, y, _ = state
    a, b, _ = goal
    if (x,y) == (a,b):
        return True
    else:
        return False
    
def finish():
    print("Maze complete!")

rules = [
    Rule(condition=can_move_left, action=move_left),
    Rule(condition=can_move_up, action=move_up),
    Rule(condition=can_move_right, action=move_right),
    Rule(condition=can_move_down, action=move_down),
]