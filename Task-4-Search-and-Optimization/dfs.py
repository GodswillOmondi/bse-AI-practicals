# =========================================================
# TASK FOUR – SEARCH AND OPTIMIZATION
#  Depth First Search (DFS)
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
# DEPTH FIRST SEARCH (DFS)
# =========================================================
# DFS explores as deep as possible before backtracking.
# It uses a stack.

def dfs(graph, start, goal):

    # Stack stores tuples of (current_node, path_taken)
    stack = [(start, [start])]

    # Set to keep track of visited nodes
    visited = set()

    while stack:

        # Remove last element from stack
        current_node, path = stack.pop()

        # Check if goal node is reached
        if current_node == goal:
            return path

        # Process node only if not visited
        if current_node not in visited:

            visited.add(current_node)

            # Add neighbors to stack
            for neighbor in reversed(graph[current_node]):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None



# =========================================================
# MAIN PROGRAM
# =========================================================

# Initial node
start_node = 'A'

# Goal node
goal_node = 'H'


# Perform DFS
dfs_path = dfs(graph, start_node, goal_node)

# =========================================================
# OUTPUT RESULTS
# =========================================================
print("\n===== DEPTH FIRST SEARCH (DFS) =====")
if dfs_path:
    print("Path found:", " -> ".join(dfs_path))
else:
    print("No path found.")
