n, m = map(int, input().split())

adj_list = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    adj_list[a-1].append(b-1)
    adj_list[b-1].append(a-1)

visited = [False] * n
connected_components = []

for i in range(n):
    if not visited[i]:
        connected_component = []
        stack = [i]
        visited[i] = True
        while stack:
            vertex = stack.pop()
            connected_component.append(vertex+1)
            for neighbor in adj_list[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
        connected_components.append(connected_component)

print(len(connected_components))
for component in connected_components:
    print(len(component))
    print(*component)
