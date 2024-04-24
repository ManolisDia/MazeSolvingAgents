
# This file contains the definition of the Node class, which is used to represent nodes in a search tree.
class Node:
    def __init__(self, coordinates, g, h, f, parent):
        
        self.coordinates = coordinates
        
       # Cost from the start node to this node
        self.g = g
        
        #Heuristic - estimated cost from this node to the end node
        self.h = h
        
        # Total cost of the node (f = g + h)
        self.f = f
        
        # Parent node: the node from which this node was reached
        self.parent = parent
    

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))
    
