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
    if y + 1 < len(maze[0]) and maze[x][y + 1] == 0:  # Checks if the right cell exists and is not a wall
        if (x, y + 1) not in visited_cells_and_rules:  # Check if the cell is not visited
            return True
        else:
            return visited_cells_and_rules[(x, y + 1)] != current_rule
    return False

def move_right(state, visited_cells_and_rules, current_rule):
    x, y, maze = state
    # visited_cells_and_rules[(x, y + 1)] = current_rule
    return (x, y + 1, maze)


def can_move_left(state, visited_cells_and_rules, current_rule):
    x, y, maze = state
    # Ensure y+1 is within the width of the maze
    if y - 1 < len(maze[0]) and maze[x][y - 1] == 0:  # Checks if the right cell exists and is not a wall
        if (x, y - 1) not in visited_cells_and_rules:  # Check if the cell is not visited
            return True
        else:
            # Check if the same rule has not been used in this cell
            return visited_cells_and_rules[(x, y - 1)] != current_rule
            
    return False

def move_left(state, visited_cells_and_rules, current_rule):
    x, y, maze = state
    # visited_cells_and_rules[(x, y - 1)] = current_rule
    return (x, y - 1, maze)


def can_move_up(state, visited_cells_and_rules, current_rule):
    x, y, maze = state
    # Ensure y+1 is within the width of the maze
    if x - 1 < len(maze[0]) and maze[x - 1][y] == 0:  # Checks if the right cell exists and is not a wall
        if (x, y + 1) not in visited_cells_and_rules:  # Check if the cell is not visited
            return True
        else:
            # Check if the same rule has not been used in this cell
            return visited_cells_and_rules[(x, y + 1)] != current_rule
    return False

def move_up(state, visited_cells_and_rules, current_rule):
    x, y, maze = state
    # visited_cells_and_rules[(x - 1, y)] = current_rule
    return (x - 1, y, maze)


def can_move_down(state, visited_cells_and_rules, current_rule):
    x, y, maze = state
    # Ensure y+1 is within the width of the maze
    if x + 1 < len(maze[0]) and maze[x + 1][y] == 0:  # Checks if the right cell exists and is not a wall
        if (x + 1, y) not in visited_cells_and_rules:  # Check if the cell is not visited
            return True
        else:
            # Check if the same rule has not been used in this cell
            return visited_cells_and_rules[(x + 1, y)] != current_rule
    return False


def move_down(state, visited_cells_and_rules, current_rule):
    x, y, maze = state
    # visited_cells_and_rules[(x + 1, y)] = current_rule
    return (x + 1, y, maze)


def is_goal(state, goal):
    x, y, _ = state
    a, b, _ = goal
    if (x, y) == (a, b):
        return True
    else:
        return False