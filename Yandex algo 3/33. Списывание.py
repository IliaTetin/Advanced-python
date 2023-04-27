n, m = map(int, input().split())

adj_list = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    adj_list[a-1].append(b-1)
    adj_list[b-1].append(a-1)

visited = [-1] * n
stack = []

def dfs(start):
    visited[start] = 1
    stack.append(start)

    while stack:
        vertex = stack.pop()
        for neighbor in adj_list[vertex]:
            if visited[neighbor] == -1:
                visited[neighbor] = 1 - visited[vertex]
                stack.append(neighbor)
            elif visited[neighbor] == visited[vertex]:
                return "NO"
    return "YES"

for i in range(n):
    if visited[i] == -1:
        result = dfs(i)
        if result == "NO":
            print(result)
            break
else:
    print("YES")
