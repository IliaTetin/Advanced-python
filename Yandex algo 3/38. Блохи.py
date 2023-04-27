from collections import deque

n, m, s, t, q = map(int, input().split())

# create a board with all cells initially marked as unvisited
board = [[-1 for j in range(m)] for i in range(n)]

# mark the feeding trough cell as visited and set the distance to 0
board[s-1][t-1] = 0

# queue to hold cells to visit in BFS
queue = deque([(s-1, t-1)])

# BFS to calculate distances from the feeding trough
while queue:
    x, y = queue.popleft()
    for dx, dy in [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == -1:
            board[nx][ny] = board[x][y] + 1
            queue.append((nx, ny))

# calculate the sum of minimum distances for all fleas
total_distance = 0
for i in range(q):
    x, y = map(int, input().split())
    if board[x-1][y-1] == -1:
        # if at least one flea can't reach the feeding trough, set total distance to -1 and break
        total_distance = -1
        break
    else:
        total_distance += board[x-1][y-1]

print(total_distance)
