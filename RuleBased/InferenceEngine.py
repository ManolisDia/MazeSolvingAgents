from Labyrinth import labyrinth
#suc dic
#JUST RUN IT FROM THIS FILE IT ALL WORKS
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


class MazeExplorer:
    def __init__(self):
        self.trackedPositions = {}
        self.maze = labyrinth
        
        start_x, start_y = 0, 0
        self.origin = (start_x, start_y, tuple(map(tuple, self.maze)))
        goal_x, goal_y = 4, 5
        self.destination = (goal_x, goal_y, tuple(map(tuple, self.maze)))
        self.position = self.origin

        self.navigationRules = [
            Rule(condition=can_shift_right, action=shift_right),
            Rule(condition=can_shift_left, action=shift_left),
            Rule(condition=can_shift_up, action=shift_up),
            Rule(condition=can_shift_down, action=shift_down)
        ]

    def is_explored(self, state):
        x, y, _ = state
        return (x, y) in self.trackedPositions

    def mark_explored(self, state, rule):
        rule_id = str(rule.action.__name__)
        x, y, _ = state
        if (x, y) not in self.trackedPositions:
            self.trackedPositions[(x, y)] = set()
        self.trackedPositions[(x, y)].add(rule_id)
        print("Recorded action:", rule_id, "at location:", (x, y))

    def apply_navigation(self):
        x, y, _ = self.position
        visited_actions = self.trackedPositions.get((x, y), set())

        for rule in self.navigationRules:
            if rule.condition(self.position) and rule.action.__name__ not in visited_actions:
                new_position = rule.action(self.position)
                if not self.is_explored(new_position):
                    self.mark_explored(self.position, rule)
                    self.position = new_position
                    return rule, self.position

        print("No available moves from this position.")
        return None, None

    def show_maze(self):
        maze_display = [list(row) for row in self.maze]
        x, y, _ = self.position
        maze_display[x][y] = 'A'
        for (vx, vy), actions in self.trackedPositions.items():
            if (vx, vy) != (x, y):
                maze_display[vx][vy] = 'V'
        for row in maze_display:
            print(' '.join(str(cell) for cell in row))
        print()

    def explore_maze(self):
        while True:
            self.show_maze()
            print("Current location: (x={}, y={})".format(self.position[1], self.position[0]))
            if is_destination(self.position, self.destination):
                print("Maze successfully solved!")
                return True
            rule, new_position = self.apply_navigation()
            if new_position is None:
                print("Cannot solve the maze!")
                return False
solver = MazeExplorer()
solver.explore_maze()