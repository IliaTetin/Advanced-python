# Дан список. Определите, является ли он монотонно возрастающим(то есть верно ли, что каждый элемент этого списка больше предыдущего).
# Выведите YES, если массив монотонно возрастает и NO в противном случае.

# Input 1 7 9
# Output YES

def growing_list(arr):
    L = len(arr)
    if L == 1:
        return 'YES'
    prev = arr[0]
    for i in range(1, L):
        if arr[i] <= prev:
            return 'NO'
        prev = arr[i]
    return 'YES'


arr = list(map(int, input().split()))
print(growing_list(arr))
