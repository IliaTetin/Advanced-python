import sys
sys.setrecursionlimit(100000)

inf = 1000000

def dp(i, j, dp_table, cost_list):
    if j > i:
        return inf
    elif dp_table[i][j] != -1:
        return dp_table[i][j]
    else:
        cost = cost_list[i]
        if j <= 0:
            if i >= 1:
                if cost <= 100:
                    dif = min(dp(i-1, j+1, dp_table, cost_list), dp(i-1, j, dp_table, cost_list) + cost)
                    res = dif
                else:
                    res = dp(i-1, j+1, dp_table, cost_list)
            else:
                res = 0
        else:
            if cost > 100:
                dif = min(dp(i-1, j+1, dp_table, cost_list), dp(i-1, j-1, dp_table, cost_list) + cost)
                res = dif
            else:
                dif = min(dp(i-1, j+1, dp_table, cost_list), dp(i-1, j, dp_table, cost_list) + cost)
                res = dif
        dp_table[i][j] = res
        return res


def find_used_days(used_list, i, j, dp_table, cost_list):
    if j < i:
        cost = cost_list[i]
        if j <= 0:
            if i >= 1:
                if cost > 100:
                    used_list.append(i)
                    find_used_days(used_list, i-1, j+1, dp_table, cost_list)
                else:
                    addi = (dp(i, j, dp_table, cost_list) == dp(i-1, j+1, dp_table, cost_list))
                    if addi:
                        used_list.append(i)
                        find_used_days(used_list, i-1, j+1, dp_table, cost_list)
                    else:
                        find_used_days(used_list, i-1, j, dp_table, cost_list)
            else:
                return
        else:
            if cost <= 100:
                addi = (dp(i-1, j+1, dp_table, cost_list) == dp(i, j, dp_table, cost_list))
                if addi:
                    used_list.append(i)
                    find_used_days(used_list, i-1, j+1, dp_table, cost_list)
                else:
                    find_used_days(used_list, i-1, j, dp_table, cost_list)
            else:
                addi = (dp(i-1, j+1, dp_table, cost_list) == dp(i, j, dp_table, cost_list))
                if addi:
                    used_list.append(i)
                    find_used_days(used_list, i-1, j+1, dp_table, cost_list)
                else:
                    find_used_days(used_list, i-1, j-1, dp_table, cost_list)



n = int(input())
k1 = 0
k2 = 0
cost_list = [0] * (n+1)
for i in range(1, n+1):
    cost_list[i] = int(input())
dp_table  = [[-1] * (n+2) for _ in range(n+1)]

ans = inf

for i in range(n+1):
    if ans >= dp(n, i, dp_table, cost_list):
        ans = dp(n, i, dp_table, cost_list)
        k1 = i

print(ans)

used = []
find_used_days(used, n, k1, dp_table, cost_list)

k2 = len(used)

print(k1, k2)
for day in reversed(used):
    print(day)
