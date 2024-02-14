from def_maze import maze

class Problem:

    def __init__(self, maze, initial, goal):
        self.initial = initial
        self.maze = maze
        self.goal = goal

    def actions(self, coordinates):
        actions = []
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Up, Down, Left, Right
        for dx, dy in directions:
            next_coordinates = (coordinates[0] + dx, coordinates[1] + dy)
            if 0 <= next_coordinates[0] < len(self.maze) and 0 <= next_coordinates[1] < len(self.maze[0]) and self.maze[next_coordinates[0]][next_coordinates[1]] == 0:
                actions.append((dx, dy))
        return actions

    def result(self, coordinates, action):
        return (coordinates[0] + action[0], coordinates[1] + action[1])


    def goal_test(self, coordinates):
        return coordinates == self.goal

    def path_cost(self, c, coordinates1, action, coordinates2):
        return c + 1
    
    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))