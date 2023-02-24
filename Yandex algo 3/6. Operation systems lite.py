n = int(input())
m = int(input())

partitions = []
for i in range(m):
    a, b = map(int, input().split())
    partitions.append((a, b))

valid_partitions = [True] * m

for i in range(1, m):
    for j in range(i):
        if partitions[i][0] <= partitions[j][1] and partitions[i][1] >= partitions[j][0]:
            valid_partitions[j] = False

print(sum(valid_partitions))
