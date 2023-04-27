from collections import deque

# Read data
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
start, end = map(int, input().split())

# BFS
visited = [False] * n
queue = deque([(start - 1, 0)])  # Store vertices and distances
visited[start - 1] = True
while queue:
    node, distance = queue.popleft()
    if node == end - 1:
        print(distance)
        break
    for neighbor in range(n):
        if graph[node][neighbor] and not visited[neighbor]:
            visited[neighbor] = True
            queue.append((neighbor, distance + 1))
else:
    print(-1)
