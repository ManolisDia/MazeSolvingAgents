from def_maze import maze
from def_maze import calculate_manhattan_distance

# from def_maze import manhattan_distances
from def_node import Node


# A* search algorithm
def astar_search(maze, initial, goal):
    """
    A* search algorithm to find the shortest path from the initial node to the goal node in a maze.

    Args:
        maze (list): The maze represented as a 2D list, where 0 represents an empty cell and 1 represents a wall.
        initial (tuple): The coordinates of the initial node in the maze.
        goal (tuple): The coordinates of the goal node in the maze.

    Returns:
        Node: The goal node if a path is found, None otherwise.
    """

    # g is the cost of the path from the start node to the current node which for the start node is zero
    g_start = 0

    # h is the heuristic which is the estimated cost from the current node to the end node
    h_start = calculate_manhattan_distance(initial[0], initial[1], goal[0], goal[1])

    # f is the total cost of the node
    f_start = g_start + h_start

    # create the start node
    start_node = Node(initial, g_start, h_start, f_start, None)

    # create the open list and add the start node - FRONTIER LIST
    open_list = [start_node]

    # create the closed list - EXPLORED LIST
    closed = []

    i = 0

    # FRONTIER
    while open_list != []:

        i += 1
        # find the node in the open list with the lowest f value
        # what is the f value? f = g + h where g is the cost from the start node to the current node and h is the
        # heuristic estimated cost from the current node to the end node
        # Select the node with the lowest F cost
        current_node = min(open_list, key=lambda node: node.f)
        print(
            "current node: ",
            current_node.coordinates,
            " current node g: ",
            current_node.g,
            " current node h: ",
            current_node.h,
            " current node f: ",
            current_node.f,
        )

        # remove the current node from the open list and add it to the closed list
        open_list.remove(current_node)
        closed.append(current_node)

        # if the current node is the goal, return the current node
        if current_node.coordinates == goal:
            print("goal coordinate is:", current_node.coordinates)
            solvedMaze = [row[:] for row in maze]
            print("Solved maze visualised:")
            for node in current_node.path():
                x, y = (
                    node.coordinates
                )  # Assuming node.coordinates returns a tuple (row, col)
                solvedMaze[x][y] = 2  # Mark the path

            for row in solvedMaze:
                print(row)

            return current_node

        # identifying neighbors
        for new_coordinates in [
            (1, 0),
            (0, 1),
            (0, -1),
            (-1, 0),
        ]:  # neighbors are +1y, +1x, -1x, -1y
            # get node coordinates
            node_coordinates = (
                current_node.coordinates[0] + new_coordinates[0],
                current_node.coordinates[1] + new_coordinates[1],
            )

            # checking that the node is within the maze and is not a wall
            if (
                0 <= node_coordinates[1] < len(maze[0])  # rows y
                and 0 <= node_coordinates[0] < len(maze)  # columns x
                # check if the node is not a wall
                and maze[node_coordinates[0]][node_coordinates[1]] == 0
            ):

                # create cost of the path from the start node to the current node
                g_new = current_node.g + 1
                h_new = calculate_manhattan_distance(
                    node_coordinates[0], node_coordinates[1], goal[0], goal[1]
                )
                f_new = g_new + h_new

                # create the new node
                new_node = Node(node_coordinates, g_new, h_new, f_new, current_node)

                # check if this node is in the closed that already made check if new coord exists with lower g value in closed list
                in_closed = any(
                    node
                    for node in closed
                    if node.coordinates == new_node.coordinates and node.g <= new_node.g
                )

                if not in_closed:
                    # Check if this node is in the open list with a lower g value
                    existing_node = next(
                        (
                            node
                            for node in open_list
                            if node.coordinates == new_node.coordinates
                        ),
                        None,
                    )
                    if existing_node is None or existing_node.g > new_node.g:
                        if existing_node:
                            open_list.remove(existing_node)
                        open_list.append(new_node)

                print(
                    "open list coordinates: ", [node.coordinates for node in open_list]
                )
                print(
                    "closed list coordinates: ", [node.coordinates for node in closed]
                )
                if open_list == []:
                    print("No path found")
                print("End of iteration number: ", i)


"""UPDATE THE CODE BELOW DEPENDING ON THE MAZE YOU ARE USING
"""
astar_search(maze, (0, 0), (4, 5))
