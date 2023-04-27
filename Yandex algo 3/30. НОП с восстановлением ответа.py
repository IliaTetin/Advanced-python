n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# create a 2D array to store the lengths of the common subsequences
dp = [[0] * (m+1) for _ in range(n+1)]

# fill the first row and column with 0s
for i in range(n+1):
    dp[i][0] = 0
for j in range(m+1):
    dp[0][j] = 0

# fill in the rest of the array using dynamic programming
for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# backtrack through the array to find the actual common subsequence
ans = []
i = n
j = m
while i > 0 and j > 0:
    if a[i-1] == b[j-1]:
        ans.append(a[i-1])
        i -= 1
        j -= 1
    elif dp[i-1][j] >= dp[i][j-1]:
        i -= 1
    else:
        j -= 1

# reverse the answer list and print it
ans.reverse()
print(*ans)
