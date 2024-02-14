from def_maze import maze
from def_maze import calculate_manhattan_distance
from def_maze import manhattan_distances
from def_node import Node

initial = (0, 0)
goal = (4, 5)

def astar_search(maze, initial, goal):

    g_start = 0
    h_start = calculate_manhattan_distance(0,0,4,5)
    f_start = g_start + h_start

    start_node = Node(initial, g_start, h_start, f_start, None)
    

    open_list = [start_node]

    closed = []


    while open_list != []:
        current_node = min(open_list, key=lambda node: node.f)
        open_list.remove(current_node)
        closed.append(current_node)
        if current_node.coordinates == goal:
            print(current_node.coordinates)
            return current_node

        for new_coordinates in [(0, -1), (0, 1), (-1, 0), (1, 0)]: 
            node_coordinates = (current_node.coordinates[0] + new_coordinates[0], current_node.coordinates[1] + new_coordinates[1])
            
            mazeX = 

            if (0 <= node_coordinates[0] < len(maze) 
                and 
                0<= node_coordinates[1] < len(maze) 
                and 
                maze[node_coordinates[0], node_coordinates[1] != 1]
            ):
                g_new = current_node.g + 1
                h_new = calculate_manhattan_distance(node_coordinates[0], node_coordinates[1], goal[0], goal[1])
                f_new = g_new + h_new

                new_node = Node(node_coordinates, g_new, h_new, f_new, current_node)
                print(new_node.coordinates)
    
    #print(current_node.coordinates)



astar_search(maze, (0, 0), (4, 5))