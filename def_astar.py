from def_maze import maze
from def_maze import calculate_manhattan_distance
from def_maze import manhattan_distances
from def_node import Node

# A* search algorithm
def astar_search(maze, initial, goal):

    #g is the cost of the path from the start node to the current node which for the start node is zero
    g_start = 0
    #h is the heuristic which is the estimated cost from the current node to the end node
    h_start = calculate_manhattan_distance(0,0,4,5)
    #f is the total cost of the node
    f_start = g_start + h_start

    #create the start node
    start_node = Node(initial, g_start, h_start, f_start, None)
    
    #create the open list and add the start node
    open_list = [start_node]
    #create the closed list
    closed = []

    i = 0
    
    while open_list != [] :
        
        #i += 1
        #find the node in the open list with the lowest f value
        current_node = min(open_list, key=lambda node: node.f)
        #print("current node: ", current_node.coordinates)
        #print("current node g: ", current_node.g)
        #print("current node h: ", current_node.h)   
        #print("current node f: ", current_node.f)
    

        #remove the current node from the open list
        open_list.remove(current_node)
        #print("removing", current_node.coordinates, "from open list")

        #add the current node to the closed list
        closed.append(current_node)
        #print("adding", current_node.coordinates, "to closed list") 

        print("current node: ", current_node.coordinates)
        #if the current node is the goal, return the current node
        if current_node.coordinates == goal:
            print("goal coordinate is:",current_node.coordinates)
            print ("goal path is:", current_node.path())
            return current_node
        
        #identifying neighbors
        for new_coordinates in [ (1, 0), (0, 1), (0, -1), (-1, 0)]: #neighbors are +1y, +1x, -1x, -1y 
            #get node coordinates
            node_coordinates = (current_node.coordinates[0] + new_coordinates[0], current_node.coordinates[1] + new_coordinates[1])
            
            #checking that the node is within the maze and is not a wall
            if (0 <= node_coordinates[1] < len(maze[0]) #rows y
                and 
                0<= node_coordinates[0] < len(maze) #columns x
                and 
                maze[node_coordinates[0]][node_coordinates[1]] == 0
            ):
                
                #print("node coordinates: ", node_coordinates)  
                g_new = current_node.g + 1
                #print("g_new: ", g_new)
                h_new = calculate_manhattan_distance(node_coordinates[0], node_coordinates[1], goal[0], goal[1])
                #print("h_new: ", h_new)
                f_new = g_new + h_new
                #print("f_new: ", f_new)

                new_node = Node(node_coordinates, g_new, h_new, f_new, current_node)

                #print("new node: ", new_node.coordinates)   

                in_closed = any(node for node in closed if node.coordinates == new_node.coordinates and node.g <= new_node.g)

                if not in_closed:
                    # Check if this node is in the open list with a lower g value
                    existing_node = next((node for node in open_list if node.coordinates == new_node.coordinates), None)
                    if existing_node is None or existing_node.g > new_node.g:
                        if existing_node:
                            open_list.remove(existing_node)
                            #print("removing", existing_node.coordinates, "from open list")
                        open_list.append(new_node)
                        #print("adding", new_node.coordinates, "to open list")
                
                #print ("open list: ", open_list) 
                #print ("closed list: ", closed)    
                
                

                
    
    #print(current_node.coordinates)



astar_search(maze, (0, 0), (4, 5))