class Heap:
    def __init__(self):
        self.data = []
    
    def insert(self, k):
        self.data.append(k)
        i = len(self.data) - 1
        while i > 0 and self.data[i] > self.data[(i - 1) // 2]:
            self.data[i], self.data[(i - 1) // 2] = self.data[(i - 1) // 2], self.data[i]
            i = (i - 1) // 2
    
    def extract(self):
        if len(self.data) == 1:
            return self.data.pop()
        max_val = self.data[0]
        self.data[0] = self.data.pop()
        i = 0
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < len(self.data) and self.data[left] > self.data[largest]:
                largest = left
            if right < len(self.data) and self.data[right] > self.data[largest]:
                largest = right
            if largest == i:
                break
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            i = largest
        return max_val
    
def heapify(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        j = i
        while True:
            left = 2 * j + 1
            right = 2 * j + 2
            largest = j
            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right
            if largest == j:
                break
            arr[j], arr[largest] = arr[largest], arr[j]
            j = largest
    return arr

n = int(input())
heap = Heap()
for i in range(n):
    command = input().split()
    if command[0] == '0':
        heap.insert(int(command[1]))
    elif command[0] == '1':
        print(heap.extract())

