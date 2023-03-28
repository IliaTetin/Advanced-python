N, k = map(int, input().split())

# Initialize a list to store the number of ways to reach each cell of the board
num_ways = [0] * (N+1)

# Base case: there is only one way to reach the first cell
num_ways[1] = 1

# For each cell i from 2 to N, compute the number of ways to reach it as the sum of the number of ways
# to reach the previous k cells, taking into account the board boundary
for i in range(2, N+1):
    for j in range(1, k+1):
        if i-j >= 1:
            num_ways[i] += num_ways[i-j]

# Print the number of ways to reach the last cell
print(num_ways[N])
