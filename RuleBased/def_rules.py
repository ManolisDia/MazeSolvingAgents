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
    x, y, maze = state
    maze_width = len(maze[0])
    if y + 1 < maze_width and maze[x][y + 1] == 0:
        return True
    return False


def move_right(state):
    x, y, maze = state
    return (x, y + 1, maze)


def can_move_left(state):
    x, y, maze = state
    if y > 0 and maze[x][y - 1] == 0:
        return True
    return False

def move_left(state):
    x, y, maze = state
    return (x, y - 1, maze)


def can_move_up(state):
    x, y, maze = state
    if x > 0 and maze[x - 1][y] == 0:
        return True
    return False

def move_up(state):
    x, y, maze = state
    return (x - 1, y, maze)


def can_move_down(state):
    x, y, maze = state
    maze_height = len(maze)
    if x + 1 < maze_height and maze[x + 1][y] == 0:
        return True
    return False



def move_down(state):
    x, y, maze = state
    return (x + 1, y, maze)


def is_goal(state, goal):
    x, y, _ = state
    a, b, _ = goal
    if (x, y) == (a, b):
        return True
    else:
        return False