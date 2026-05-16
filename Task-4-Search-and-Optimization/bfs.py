# =========================================================
# TASK FOUR – SEARCH AND OPTIMIZATION
# Breadth First Search (BFS)
# =========================================================

# Graph represented using an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

# =========================================================
# BREADTH FIRST SEARCH (BFS)
# =========================================================
# BFS explores nodes level by level using a queue.

from collections import deque

def bfs(graph, start, goal):

    # Queue stores tuples of (current_node, path_taken)
    queue = deque([(start, [start])])

    # Set to keep track of visited nodes
    visited = set()

    while queue:

        # Remove first element from queue
        current_node, path = queue.popleft()

        # Check if goal node is reached
        if current_node == goal:
            return path

        # Mark node as visited
        visited.add(current_node)

        # Visit neighboring nodes
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None




# =========================================================
# MAIN PROGRAM
# =========================================================

# Initial node
start_node = 'A'

# Goal node
goal_node = 'H'

# Perform BFS
bfs_path = bfs(graph, start_node, goal_node)


# =========================================================
# OUTPUT RESULTS
# =========================================================

print("===== BREADTH FIRST SEARCH (BFS) =====")
if bfs_path:
    print("Path found:", " -> ".join(bfs_path))
else:
    print("No path found.")
