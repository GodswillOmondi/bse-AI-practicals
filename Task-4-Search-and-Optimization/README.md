# TASK FOUR – SEARCH AND OPTIMIZATION
## Breadth First Search (BFS) and Depth First Search (DFS)

---

# Introduction

Search algorithms are techniques used in Artificial Intelligence and Computer Science to traverse or search through data structures such as graphs and trees.  

In this assignment, two search techniques are implemented using Python:

1. Breadth First Search (BFS)
2. Depth First Search (DFS)

Both algorithms are used to find a path from a starting node to a goal node in a graph.

---

# Graph Used in the Assignment

The graph is represented using an adjacency list.

```python
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
```

---

# Graph Structure

```text
        A
      /   \
     B     C
   /   \  / \
  D    E F   G
        |
        H
```

---

# 1. Breadth First Search (BFS)

## Definition

Breadth First Search (BFS) is a graph traversal algorithm that explores nodes level by level before moving deeper into the graph.

It uses a **Queue (FIFO – First In First Out)** data structure.

---

## How BFS Works

1. Start from the initial node.
2. Visit all neighboring nodes first.
3. Move to the next level of neighbors.
4. Continue until the goal node is found.

---

## BFS Python Code

```python
from collections import deque

def bfs(graph, start, goal):

    queue = deque([(start, [start])])
    visited = set()

    while queue:

        current_node, path = queue.popleft()

        if current_node == goal:
            return path

        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None
```

---

## BFS Output

```text
===== BREADTH FIRST SEARCH (BFS) =====
Path found: A -> B -> E -> H
```

---

## Advantages of BFS

- Finds the shortest path in an unweighted graph.
- Simple and easy to understand.

---

## Disadvantages of BFS

- Uses more memory because many nodes are stored in the queue.
- Can be slower for large graphs.

---

# 2. Depth First Search (DFS)

## Definition

Depth First Search (DFS) is a graph traversal algorithm that explores one branch deeply before backtracking.

It uses a **Stack (LIFO – Last In First Out)** data structure.

---

## How DFS Works

1. Start from the initial node.
2. Move deeply into one branch.
3. If no further nodes exist, backtrack.
4. Continue until the goal node is found.

---

## DFS Python Code

```python
def dfs(graph, start, goal):

    stack = [(start, [start])]
    visited = set()

    while stack:

        current_node, path = stack.pop()

        if current_node == goal:
            return path

        if current_node not in visited:

            visited.add(current_node)

            for neighbor in reversed(graph[current_node]):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None
```

---

## DFS Output

```text
===== DEPTH FIRST SEARCH (DFS) =====
Path found: A -> B -> E -> H
```

---

# Comparison Between BFS and DFS

| Feature | BFS | DFS |
|---|---|---|
| Data Structure | Queue | Stack |
| Traversal Style | Level by level | Depth first |
| Shortest Path | Yes | Not guaranteed |
| Memory Usage | High | Lower |
| Speed | Slower in large graphs | Faster in some cases |

---

# Main Program

```python
start_node = 'A'
goal_node = 'H'

bfs_path = bfs(graph, start_node, goal_node)
dfs_path = dfs(graph, start_node, goal_node)

print("===== BREADTH FIRST SEARCH (BFS) =====")
print("Path found:", " -> ".join(bfs_path))

print("\n===== DEPTH FIRST SEARCH (DFS) =====")
print("Path found:", " -> ".join(dfs_path))
```

---

# Conclusion

In this assignment, Breadth First Search (BFS) and Depth First Search (DFS) were successfully implemented using Python.

- BFS searches level by level and guarantees the shortest path.
- DFS explores deeper paths first and uses less memory.

Both algorithms are important in Artificial Intelligence, networking, path finding, and problem-solving systems.

---
