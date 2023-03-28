from queue import Queue

q = Queue()

while True:
    try:
        command = input().strip().split()
        if command[0] == 'push':
            q.put(int(command[1]))
            print('ok')
        elif command[0] == 'pop':
            if not q.empty():
                print(q.get())
            else:
                print('error')
        elif command[0] == 'front':
            if not q.empty():
                print(q.queue[0])
            else:
                print('error')
        elif command[0] == 'size':
            print(q.qsize())
        elif command[0] == 'clear':
            while not q.empty():
                q.get()
            print('ok')
        elif command[0] == 'exit':
            print('bye')
            break
        else:
            print('Unknown command')
    except Exception as e:
        print('Error:', e)
