n = int(input())
way = list(map(int, input().split()))
top = -1
next_wagon_idx = 0
expected_wagon = 1
stack = [0] * len(way)
num_wagons = len(way)

while next_wagon_idx != num_wagons or (top != -1 and stack[top] == expected_wagon):
    if top != -1 and stack[top] == expected_wagon:
        top -= 1
        expected_wagon += 1
    else:
        top += 1
        stack[top] = way[next_wagon_idx]
        next_wagon_idx += 1

if expected_wagon == num_wagons + 1:
    print("YES")
else:
    print("NO")
