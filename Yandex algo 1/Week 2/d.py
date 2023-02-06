# Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей и выведите количество таких элементов. 

# Input: 1 5 1 5 1
# Output: 2

def neigh(arr):
    out = 0
    if len(arr) < 3:
        return out
    
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            out += 1
    return out


arr = list(map(int, input().split()))
print(neigh(arr))
