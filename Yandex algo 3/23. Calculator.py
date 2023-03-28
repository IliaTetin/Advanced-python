N = int(input())

# Initialize a list to store the minimum number of operations required to get to each number from 1 to N
min_ops = [0] * (N+1)

# Initialize a list to store the previous number in the optimal path to each number from 1 to N
prev_num = [0] * (N+1)

# Base case: to get from 1 to 1, no operations are needed
min_ops[1] = 0

# For each number from 2 to N, find the minimum number of operations needed to get to it
# and the previous number in the optimal path
for i in range(2, N+1):
    # Initialize the minimum number of operations to the number of operations to get to i-1
    min_ops[i] = min_ops[i-1] + 1
    prev_num[i] = i-1
    
    # Check if multiplying by 2 or 3 produces a smaller number of operations
    if i % 2 == 0 and min_ops[i//2] < min_ops[i]:
        min_ops[i] = min_ops[i//2] + 1
        prev_num[i] = i//2
    if i % 3 == 0 and min_ops[i//3] < min_ops[i]:
        min_ops[i] = min_ops[i//3] + 1
        prev_num[i] = i//3

# Print the minimum number of operations to get to N
print(min_ops[N])

# Print the sequence of numbers obtained by following the optimal path
sequence = [N]
while sequence[-1] != 1:
    sequence.append(prev_num[sequence[-1]])
sequence.reverse()
print(' '.join(map(str, sequence)))
