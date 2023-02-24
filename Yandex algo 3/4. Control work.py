import math

def dist(i, row, col):
    r, c = i // 2, i % 2
    return abs(r - row) * 4 + abs(col - c) * 2 + (r < row)

n = int(input())   # the size of the game board
k = int(input())   # the number of moves
row = int(input())  # the initial row of the player
col = int(input())  # the initial column of the player

row -= 1
col -= 1

r2 = row * 2 + col + k
r3 = row * 2 + col - k
if r2 >= n or (r3 >= 0 and dist(r2, row, col) > dist(r3, row, col)):
    r2 = r3

if r2 < 0 or r2 >= n * 2:
    print("-1")
else:
    print((r2 // 2) + 1, (r2 % 2) + 1)
