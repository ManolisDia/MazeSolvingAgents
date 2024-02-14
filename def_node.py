
# This file contains the definition of the Node class, which is used to represent nodes in a search tree.
class Node:
    def __init__(self, coordinates, g, h, f, parent):
        # Coordinates (e.g., (x, y) in a grid)
        self.coordinates = coordinates
        
        # g: Cost from the start node to this node
        self.g = g
        
        # h: Heuristic - estimated cost from this node to the end node
        self.h = h
        
        # f: Total cost of the node (f = g + h)
        self.f = f
        
        # Parent node: the node from which this node was reached
        self.parent = parent
    
    
    def __repr__(self):
        return "<Node {}>".format(self.coordinates)
    
    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.coordinates)]
    
    def child_node(self, problem, action):
        """[Figure 3.10]"""
        next_coordinates = problem.result(self.coordinates, action)
        next_node = Node(next_coordinates, self, action, problem.path_cost(self.path_cost, self.coordinates, action, next_coordinates))
        return next_node
    
    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))
    
