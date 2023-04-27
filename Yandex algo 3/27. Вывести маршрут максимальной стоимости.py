N, M = map(int, input().split())
value = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(M)] for _ in range(N)]
path = [['' for _ in range(M)] for _ in range(N)]
dp[0][0] = value[0][0]

# Fill out first row and column of dp
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + value[0][j]
    path[0][j] = 'R'
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + value[i][0]
    path[i][0] = 'D'

# Fill out the rest of dp and path
for i in range(1, N):
    for j in range(1, M):
        if dp[i-1][j] >= dp[i][j-1]:
            dp[i][j] = dp[i-1][j] + value[i][j]
            path[i][j] = 'D'
        else:
            dp[i][j] = dp[i][j-1] + value[i][j]
            path[i][j] = 'R'

# Reconstruct the path
i, j = N-1, M-1
route = ''
while i > 0 or j > 0:
    route = path[i][j] + route
    if path[i][j] == 'D':
        i -= 1
    else:
        j -= 1

print(dp[N-1][M-1])
print(route)
