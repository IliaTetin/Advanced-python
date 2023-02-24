n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
cumulative_sum = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        cumulative_sum[i][j] = cumulative_sum[i-1][j] + cumulative_sum[i][j-1] - cumulative_sum[i-1][j-1] + matrix[i-1][j-1]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    print(cumulative_sum[x2][y2] - cumulative_sum[x1-1][y2] - cumulative_sum[x2][y1-1] + cumulative_sum[x1-1][y1-1])
