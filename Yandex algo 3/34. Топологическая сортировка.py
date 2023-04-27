from collections import deque

n, m = map(int, input().split())

in_degree = [0] * n
adj_list = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    adj_list[a-1].append(b-1)
    in_degree[b-1] += 1

queue = deque([i for i in range(n) if in_degree[i] == 0])
topological_sort = []

while queue:
    vertex = queue.popleft()
    topological_sort.append(vertex)
    for neighbor in adj_list[vertex]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

if len(topological_sort) != n:
    print(-1)
else:
    print(*[i+1 for i in topological_sort])
