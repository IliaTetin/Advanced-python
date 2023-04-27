n = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(n)]

adj_list = [[] for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        if adj_matrix[i][j] == 1:
            adj_list[i].append(j)
            adj_list[j].append(i)

cycle = []

def dfs(vertex, parent):
    visited[vertex] = True
    for neighbor in adj_list[vertex]:
        if not visited[neighbor]:
            parent[neighbor] = vertex
            if dfs(neighbor, parent):
                return True
        elif neighbor != parent[vertex]:
            current = vertex
            while current != neighbor:
                cycle.append(current)
                current = parent[current]
            cycle.append(neighbor)
            cycle.reverse()
            return True
    return False

visited = [False] * n
parent = [-1] * n

for i in range(n):
    if not visited[i] and dfs(i, parent):
        break

if not cycle:
    print("NO")
else:
    start = cycle[-1]
    cycle = cycle[cycle.index(start):] + cycle[:cycle.index(start)]
    print("YES")
    print(len(cycle))
    print(*[v+1 for v in cycle])
