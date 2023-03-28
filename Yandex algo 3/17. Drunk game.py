from collections import deque

a = deque(map(int, input().split()))
b = deque(map(int, input().split()))

winner = 0
moves = 0

while moves < 1000000 and a and b:
    moves += 1
    ac = a.popleft()
    bc = b.popleft()

    if ac == 0 and bc == 9:
        a.append(ac)
        a.append(bc)
    elif bc == 0 and ac == 9:
        b.append(ac)
        b.append(bc)
    elif ac > bc:
        a.append(ac)
        a.append(bc)
    else:
        b.append(ac)
        b.append(bc)

    if not a:
        winner = 2
    if not b:
        winner = 1

if not winner:
    print('botva')
elif winner == 1:
    print('first', moves)
else:
    print('second', moves)
    