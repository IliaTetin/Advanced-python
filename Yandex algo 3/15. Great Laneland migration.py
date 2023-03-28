from typing import List
from collections import deque

n = int(input())

input_arr = list(map(int, input().split()))
n = len(input_arr)

nums = deque([-1])
costs = deque([-1])

ans = [-1] * n

for i in range(n):
    cost = input_arr[i]
    while cost < costs[-1]:
        ans[nums[-1]] = i
        costs.pop()
        nums.pop()
    costs.append(cost)
    nums.append(i)

print(*ans)
