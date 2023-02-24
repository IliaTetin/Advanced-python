n = int(input())
counts = [int(input()) for _ in range(n)]
ans = 0
for i in range(n-1):
    if counts[i] < counts[i+1]:
        ans += counts[i]
    else:
        ans += counts[i+1]
print(ans)
