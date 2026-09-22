import time
from bfs_dfs import bfs, dfs, graph

start = 'A'
goal = 'Z'

# BFS
start_time = time.perf_counter()
bfs_nodes = bfs(graph, start, goal)
end_time = time.perf_counter()

bfs_time = (end_time - start_time) * 1000

# DFS
start_time = time.perf_counter()
dfs_nodes = dfs(graph, start, goal)
end_time = time.perf_counter()

dfs_time = (end_time - start_time) * 1000

print("BFS PERFORMANCE")
print("----------------")
print("BFS Nodes Explored:", bfs_nodes)
print(f"BFS Execution Time: {bfs_time:.6f} ms")

print("\nDFS PERFORMANCE")
print("----------------")
print("DFS Nodes Explored:", dfs_nodes)
print(f"DFS Execution Time: {dfs_time:.6f} ms")