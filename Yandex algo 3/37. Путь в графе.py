import sys
from collections import deque

def bfs(start, end):
    queue = deque([start])
    parents = {start: None}
    while queue:
        node = queue.popleft()
        if node == end:
            path = []
            while node is not None:
                path.append(node)
                node = parents[node]
            path.reverse()
            return path
        for neighbor in range(n):
            if graph[node][neighbor] and neighbor not in parents:
                parents[neighbor] = node
                queue.append(neighbor)
    return None

# Read input
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
start, end = map(int, input().split())

# Find shortest path using BFS
path = bfs(start - 1, end - 1)

# Print output
if path is None:
    print(-1)
else:
    print(len(path) - 1)
    if (len(path) - 1) != 0:
        print(*[x + 1 for x in path])
