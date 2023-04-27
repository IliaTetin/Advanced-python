from collections import deque

# read input
n = int(input())
levels = []
for _ in range(n):
    input()
    level = []
    for _ in range(n):
        row = input().strip()
        level.append(list(row))
        if 'S' in row:
            start_x, start_y, start_z = _, row.index('S'), len(levels)
    levels.append(level)

# BFS
q = deque([(start_x, start_y, start_z, 0)])
visited = set([(start_x, start_y, start_z)])
steps = -1
while q:
    x, y, z, dist = q.popleft()
    if z == 0:
        # found exit to surface
        steps = dist
        break
    for dx, dy, dz in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
        nx, ny, nz = x + dx, y + dy, z + dz
        if 0 <= nx < n and 0 <= ny < n and 0 <= nz < n and levels[nz][nx][ny] == '.' and (nx, ny, nz) not in visited:
            visited.add((nx, ny, nz))
            q.append((nx, ny, nz, dist+1))

if steps == -1:
    print(-1)
else:
    print(steps)
