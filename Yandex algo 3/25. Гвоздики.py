import random

n = int(input())
pos = [0] + [int(i) for i in input().split()]
pos.sort()

dp = [[0, 0] for i in range(n + 1)]
dp[1] = [10**9, 0]

for i in range(2, n + 1):
    dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + (pos[i] - pos[i - 1])
    dp[i][1] = dp[i - 1][0]

print(dp[n][0])
