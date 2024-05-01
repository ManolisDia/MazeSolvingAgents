from Labyrinth import labyrinth

# Author : Brandon Eddy


class Rule:
    """
    Represents a rule in an inference engine.

    Attributes:
        condition (function): A function that takes a state and returns a boolean indicating whether the rule applies to the state.
        action (function): A function that takes a state and performs the action associated with the rule.

    Methods:
        applies(state): Checks if the rule applies to the given state.
        perform(state): Performs the action associated with the rule on the given state.
    """

    def __init__(self, condition, action):
        self.condition = condition
        self.action = action

    def applies(self, state):
        """
        Checks if the rule applies to the given state.

        Args:
            state: The state to check.

        Returns:
            bool: True if the rule applies to the state, False otherwise.
        """
        return self.condition(state)

    def perform(self, state):
        """
        Performs the action associated with the rule on the given state.

        Args:
            state: The state to perform the action on.

        Returns:
            The updated state after performing the action.
        """
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
    """
    Represents a maze explorer agent that solves a maze using rule-based navigation.

    Attributes:
        trackedPositions (dict): A dictionary to track the positions visited by the agent.
        maze (list): The maze represented as a 2D list.
        origin (tuple): The starting position of the agent in the maze.
        destination (tuple): The goal position of the agent in the maze.
        position (tuple): The current position of the agent in the maze.
        navigationRules (list): A list of navigation rules to determine the agent's next move.
        visitedPositions (set): A set to store the positions visited by the agent.

    Methods:
        is_explored(state): Checks if a state has been explored by the agent.
        mark_explored(state, rule): Marks a state as explored by the agent.
        apply_navigation(): Applies the navigation rules to determine the agent's next move.
        show_maze(): Displays the current state of the maze with the agent's position and explored positions.
        explore_maze(): Explores the maze and attempts to solve it.
    """

    def __init__(self):
        # WORKING MEMORY to store the positions visited by the agent
        self.trackedPositions = {}

        # the maze to be explored
        self.maze = labyrinth

        # the starting position of the agent
        start_x, start_y = 0, 0

        # store the initial state of the agent as a tuple (x, y, maze) where x and y are the coordinates of the agent in the maze
        self.origin = (start_x, start_y, tuple(map(tuple, self.maze)))

        """UPDATE THIS DEPENDING ON THE MAZE YOU ARE USING
        """
        # the goal position of the agent for the maze to be solved, change this to the goal position of the maze you want to solve
        goal_x, goal_y = 4, 5

        # the destination state of the agent as a tuple (x, y, maze) where x and y are the coordinates of the agent in the maze for the goal
        self.destination = (goal_x, goal_y, tuple(map(tuple, self.maze)))

        # the current position of the agent in the maze initialized to the starting position (origin)
        self.position = self.origin

        # KNOWLEDGE BASE
        # define the navigation rules for the agent to explore the maze using the movement functions and goal check function defined above
        self.navigationRules = [
            Rule(condition=can_shift_right, action=shift_right),
            Rule(condition=can_shift_left, action=shift_left),
            Rule(condition=can_shift_up, action=shift_up),
            Rule(condition=can_shift_down, action=shift_down),
        ]

    def is_explored(self, state):
        """
        Checks if a state has been explored by the agent.

        Args:
            state (tuple): The state to check.

        Returns:
            bool: True if the state has been explored, False otherwise.
        """
        x, y, _ = state
        return (x, y) in self.trackedPositions

    def mark_explored(self, state, rule):
        """
        Marks a state as explored by the agent.

        Args:
            state (tuple): The state to mark as explored.
            rule (Rule): The rule that led to the exploration of the state.
        """
        rule_id = str(rule.action.__name__)
        x, y, _ = state
        if (x, y) not in self.trackedPositions:
            self.trackedPositions[(x, y)] = set()
        self.trackedPositions[(x, y)].add(rule_id)
        print("Recorded action:", rule_id, "at location:", (x, y))

    # INFERENCE ENGINE - applies knowledge base core part of the agent to navigate the maze
    def apply_navigation(self):
        """
        Applies the navigation rules to determine the agent's next move.

        Returns:
            tuple: A tuple containing the rule that was applied and the new position of the agent.
        """

        # unpacks the current position of the agent (x, y, maze)
        x, y, _ = self.position

        # retrieve the set of actions that have been executed at the current position, to avoid repeated actions
        # if the agent has already visited the current position, it will not execute the same action again
        # preventing the agent from going in circles
        visited_actions = self.trackedPositions.get((x, y), set())

        # Apply the navigation rules to determine the next move of the agent
        # Check if the rule applies and the action has not been visited before
        for rule in self.navigationRules:
            if (
                rule.condition(self.position)
                and rule.action.__name__ not in visited_actions
            ):
                new_position = rule.action(self.position)
                self.mark_explored(self.position, rule)
                return rule, new_position

        print("Attempting to backtrack...")
        return None, None  # Trigger backtracking if no rules apply

    def show_maze(self):
        """
        Displays the current state of the maze with the agent's position and explored positions.
        """
        # Display the maze with the agent's position and visited positions
        maze_display = [list(row) for row in self.maze]

        # Display the agent's position
        x, y, _ = self.position

        # Display the agent's position and visited positions in the maze display
        maze_display[x][y] = "∂"

        # vx is the x-coordinate (row index in the maze grid) VISITED - X
        # vy is the y-coordinate (column index in the maze grid) VISITED - Y
        for (vx, vy), actions in self.trackedPositions.items():
            if (vx, vy) != (x, y):
                maze_display[vx][vy] = "V"
        for row in maze_display:
            print(" ".join(str(cell) for cell in row))
        print()

    def explore_maze(self):
        """
        Explores the maze and attempts to solve it.

        Returns:
            bool: True if the maze was successfully solved, False otherwise.
        """
        path_stack = [
            self.position
        ]  # Stack to track the path for possible backtracking

        # Explore the maze until the destination is reached or all paths are exhausted
        while path_stack:
            # Update the current position of the agent to the top of the path stack (current path)
            self.position = path_stack[-1]

            # Display the current state of the maze
            self.show_maze()
            print(
                "Current location: (x={}, y={})".format(
                    self.position[1], self.position[0]
                )
            )
            if is_destination(self.position, self.destination):
                print("Maze successfully solved!")
                return True

            # Apply the navigation rules to determine the next move of the agent and update the path stack accordingly (forward or backtrack)
            rule, new_position = self.apply_navigation()

            # Update the path stack based on the new position or backtrack if no rules apply
            if new_position:
                path_stack.append(new_position)
            else:
                path_stack.pop()  # Backtrack

            # Check if the agent has explored all possible paths and cannot reach the destination
            if not path_stack:
                print("Cannot solve the maze!")
                return False


solver = MazeExplorer()
solver.explore_maze()
