# This file contains the definition of the Node class, which is used to represent nodes in a search tree.
class Node:
    def __init__(self, coordinates, g, h, f, parent):
        """
        Initialize a Node object.

        Parameters:
        - coordinates: The coordinates of the node in the maze.
        - g: The cost from the start node to this node.
        - h: The heuristic estimated cost from this node to the end node.
        - f: The total cost of the node (f = g + h).
        - parent: The parent node, from which this node was reached.
        """
        self.coordinates = coordinates
        self.g = g
        self.h = h
        self.f = f
        self.parent = parent

    def path(self):
        """
        Return a list of nodes forming the path from the root to this node.
        """
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))
