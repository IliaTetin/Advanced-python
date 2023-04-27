n, m = map(int, input().split())

adj_list = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    adj_list[a-1].append(b-1)
    adj_list[b-1].append(a-1)

visited = [False] * n
stack = [0]
visited[0] = True

while stack:
    vertex = stack.pop()
    for neighbor in adj_list[vertex]:
        if not visited[neighbor]:
            visited[neighbor] = True
            stack.append(neighbor)

connected_component = []
for i in range(n):
    if visited[i]:
        connected_component.append(i+1)

print(len(connected_component))
print(*connected_component)