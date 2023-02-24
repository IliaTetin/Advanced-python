k = int(input())
x_min, y_min, x_max, y_max = float('inf'), float('inf'), float('-inf'), float('-inf')

for i in range(k):
    x, y = map(int, input().split())
    x_min, y_min = min(x_min, x), min(y_min, y)
    x_max, y_max = max(x_max, x), max(y_max, y)

print(x_min, y_min, x_max, y_max)
