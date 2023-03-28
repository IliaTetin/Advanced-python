from collections import deque

d = deque()

while True:
    command = input().split()
    if command[0] == 'push_front':
        d.appendleft(int(command[1]))
        print('ok')
    elif command[0] == 'push_back':
        d.append(int(command[1]))
        print('ok')
    elif command[0] == 'pop_front':
        if len(d) > 0:
            print(d.popleft())
        else:
            print('error')
    elif command[0] == 'pop_back':
        if len(d) > 0:
            print(d.pop())
        else:
            print('error')
    elif command[0] == 'front':
        if len(d) > 0:
            print(d[0])
        else:
            print('error')
    elif command[0] == 'back':
        if len(d) > 0:
            print(d[-1])
        else:
            print('error')
    elif command[0] == 'size':
        print(len(d))
    elif command[0] == 'clear':
        d.clear()
        print('ok')
    elif command[0] == 'exit':
        print('bye')
        break
