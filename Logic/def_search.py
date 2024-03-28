#Here wd define the DFS algorithm
from def_maze import *

visited = set()

i = 0
def depth_first_search(current,goal,maze):


    if is_goal(current[0], current[1], maze):
        print("Goal Reached")
        return True
    
    if is_obstacle(current[0], current[1], maze):
        return False

    visited.add(current)
    print(visited)
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dx,dy in directions:

        new_x, new_y = dx+current[0], dy+current[1]


        if is_path(new_x,new_y,maze) and (is_visited(new_x,new_y) is False) and (is_obstacle(new_x,new_y,maze) is False):
            current = (new_x,new_y)
            i = i + 1
            print(i)
            depth_first_search(current,goal,maze)


depth_first_search( (0,0) , (4,5) , maze )