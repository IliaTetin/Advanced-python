# A perfect number is a natural number equal to the sum of all its own divisors. 
# For example, the number 6 is equal to the sum of its proper divisors 1 + 2 + 3. You need to write a program that prints all perfect numbers less than n.

# Input: 30
# Output: 6 28

class Solution():
    def check(self, n):
        perfect = []
        for i in range(6, n):
            divisor = 1
            for j in range(2, i):
                if i % j == 0:
                    divisor += j
            if i == divisor:
                perfect.append(i)
        return perfect

n = int(input())
sol = Solution()
if n >= 6:
    print(*sol.check(n))
