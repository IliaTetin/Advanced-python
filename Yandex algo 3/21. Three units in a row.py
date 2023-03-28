# Get the input value of n
n = int(input())

# Initialize a list to store the values of the dynamic programming solution
# We add 4 extra values to the list to avoid index errors
dp = [0] * (n + 4)

# Set the initial values for the base cases
dp[1] = 2
dp[2] = 4
dp[3] = 7

# Compute the solution for all values of i from 4 to n
for i in range(4, n + 1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])
print(dp[n])
