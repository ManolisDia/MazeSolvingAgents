def maze_to_graph(maze):
    rows, cols = len(maze), len(maze[0])
    graph = {}

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols and maze[r][c] != 1

    for r in range(rows):
        for c in range(cols):
            if is_valid(r, c):
                # Using (r, c) as the node identifier
                node = (r, c)
                graph[node] = []

                # Check all four directions
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if is_valid(nr, nc):
                        graph[node].append((nr, nc))
    return graph


# Your maze
maze = [
    [2, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 3],
]

graph = maze_to_graph(maze)
print(graph)
