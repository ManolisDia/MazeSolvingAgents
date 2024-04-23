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
    

def can_move_right(state, visited_cells_and_rules, current_rule):
    x, y, maze = state
    if y + 1 >= 0 and maze[x][y + 1] == 0:
        if (x, y + 1) not in visited_cells_and_rules:
            return True
        else:
            return visited_cells_and_rules[(x, y - 1)] != current_rule
    return False

    
def move_right(state, visited_cells_and_rules, current_rule):
    x, y, maze = state
    #visited_cells_and_rules[(x, y + 1)] = current_rule
    return (x, y + 1, maze)
    
def can_move_left(state, visited_cells_and_rules, current_rule):
    x, y, maze = state
    if y - 1 >= 0 and maze[x][y - 1] == 0:
        if (x, y - 1) not in visited_cells_and_rules:
            return True
        else:
            return visited_cells_and_rules[(x, y - 1)] != current_rule
    return False
    
def move_left(state, visited_cells_and_rules, current_rule):
    x, y, maze = state
    #visited_cells_and_rules[(x, y - 1)] = current_rule
    return (x, y - 1, maze)


def can_move_up(state, visited_cells_and_rules, current_rule):
    x, y, maze = state
    if x - 1 >= 0 and maze[x - 1][y] == 0:
        if (x - 1, y) not in visited_cells_and_rules:
            return True
        else:
            return visited_cells_and_rules[(x - 1, y)] != current_rule
    return False

def move_up(state, visited_cells_and_rules, current_rule):
    x, y, maze = state
    #visited_cells_and_rules[(x - 1, y)] = current_rule
    return (x - 1, y, maze)

def can_move_down(state, visited_cells_and_rules, current_rule):
    x, y, maze = state
    if x + 1 < len(maze) and maze[x + 1][y] == 0:
        if (x + 1, y) not in visited_cells_and_rules:
            return True
        else:
            return visited_cells_and_rules[(x + 1, y)] != current_rule
    return False

def move_down(state, visited_cells_and_rules, current_rule):
    x, y, maze = state
    #visited_cells_and_rules[(x + 1, y)] = current_rule
    return (x + 1, y, maze)


def is_goal(state, goal):
    x, y, _ = state
    a, b, _ = goal
    if (x,y) == (a,b):
        return True
    else:
        return False
    
def can_move_right(state, visited_cells_and_rules, current_rule):
    x, y, maze = state
    if y + 1 < len(maze[0]) and maze[x][y + 1] == 0:
        if (x, y + 1) not in visited_cells_and_rules:
            #this is just checking if the cell has been visited before
            return True
        elif (x, y + 1) in visited_cells_and_rules and current_rule in visited_cells_and_rules[(x, y + 1)]:
            return "You can go here but you cant use that rule but you can try another rule"
        else:
            return "Returning False"
            
    return False