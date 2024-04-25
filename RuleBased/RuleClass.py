from InferenceEngine import *
from Labyrinth import labyrinth

class Rule:
    def __init__(self, condition, action):
        self.condition = condition
        self.action = action

    def applies(self, state):
        return self.condition(state)

    def perform(self, state):
        return self.action(state)

# Movement functions
def can_shift_right(state):
    x, y, labyrinth = state
    width = len(labyrinth[0])
    if y + 1 < width and labyrinth[x][y + 1] == 0:
        return True
    return False

def shift_right(state):
    x, y, labyrinth = state
    return (x, y + 1, labyrinth)

def can_shift_left(state):
    x, y, labyrinth = state
    if y > 0 and labyrinth[x][y - 1] == 0:
        return True
    return False

def shift_left(state):
    x, y, labyrinth = state
    return (x, y - 1, labyrinth)

def can_shift_up(state):
    x, y, labyrinth = state
    if x > 0 and labyrinth[x - 1][y] == 0:
        return True
    return False

def shift_up(state):
    x, y, labyrinth = state
    return (x - 1, y, labyrinth)

def can_shift_down(state):
    x, y, labyrinth = state
    height = len(labyrinth)
    if x + 1 < height and labyrinth[x + 1][y] == 0:
        return True
    return False

def shift_down(state):
    x, y, labyrinth = state
    return (x + 1, y, labyrinth)

# Goal check function
def is_destination(state, destination):
    x, y, _ = state
    dest_x, dest_y, _ = destination
    if (x, y) == (dest_x, dest_y):
        return True
    else:
        return False
#HI BRANDON JUST DELETE THIS FILE ON YOUR BRANCH ITS NOT NECESSARY ANY MORE CUS I MOVED IT ALL TO THE OTHER FILE