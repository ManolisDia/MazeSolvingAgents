


maze = [
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0]
]


visited = set()  

    
def is_path(x,y, maze): 
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0

def is_obstacle(x,y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1

def is_start(x,y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == maze[0][0]

def is_goal(x,y, maze):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == maze[4][5]


def mark_visited(x, y):
    visited.add((x, y))

def is_visited(x, y):
    return (x, y) in visited        