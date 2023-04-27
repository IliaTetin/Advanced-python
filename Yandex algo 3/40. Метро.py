from collections import deque

# read input
n = int(input())  # number of stations
m = int(input())  # number of lines
lines = [[] for _ in range(m)]
for i in range(m):
    line = list(map(int, input().split()))[1:]
    lines[i] = line
stations = set(x for line in lines for x in line)  # set of all stations
transfer_stations = set(x for x in stations if sum(1 for line in lines if x in line) > 1)

start, end = map(int, input().split())

# BFS
min_transfers = float('inf')
for line in lines:
    if start in line:
        q = deque([(start, 0)])
        visited = set([start])
        while q:
            curr, transfers = q.popleft()
            if curr == end:
                min_transfers = min(min_transfers, transfers)
                break
            for next in line:
                if next in visited:
                    continue
                if (curr in transfer_stations and next in transfer_stations) or next in line:  # there is a direct line between the stations or they are both transfer stations
                    visited.add(next)
                    q.append((next, transfers))
            if curr in transfer_stations:  # also try transferring at current station
                for other_line in lines:
                    if other_line == line or curr not in other_line:
                        continue
                    for next in other_line:
                        if next not in visited:
                            visited.add(next)
                            q.append((next, transfers + 1))
if min_transfers == float('inf'):
    print(-1)  # no path found
else:
    print(min_transfers)
