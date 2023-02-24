import bisect

N = int(input())
stickers = list(map(int, input().split()))
K = int(input())
pi = list(map(int, input().split()))
stickers = list(sorted(set(stickers)))

for i in range(len(pi)):
    idx = bisect.bisect_left(stickers, pi[i])
    print(idx)