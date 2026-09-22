from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': ['P', 'Q'],
    'I': ['R', 'S'],
    'J': ['T', 'U'],
    'K': ['V', 'W'],
    'L': ['X'],
    'M': ['Y'],
    'N': ['Z'],
    'O': [],
    'P': [],
    'Q': [],
    'R': [],
    'S': [],
    'T': [],
    'U': [],
    'V': [],
    'W': [],
    'X': [],
    'Y': [],
    'Z': []
}


def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()
    nodes_explored = 0

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        nodes_explored += 1

        if node == goal:
            return nodes_explored

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)

    return nodes_explored


def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    nodes_explored = 0

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes_explored += 1

        if node == goal:
            return nodes_explored

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)

    return nodes_explored


start = 'A'
goal = 'Z'

bfs_nodes = bfs(graph, start, goal)
print("BFS Nodes Explored:", bfs_nodes)

dfs_nodes = dfs(graph, start, goal)
print("DFS Nodes Explored:", dfs_nodes)