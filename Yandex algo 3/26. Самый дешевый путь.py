N, M = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = weight[0][0]

# Fill out first row and column of dp
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + weight[0][j]
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + weight[i][0]

# Fill out the rest of dp
for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + weight[i][j]

print(dp[N-1][M-1])