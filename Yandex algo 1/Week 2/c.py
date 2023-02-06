# Напишите программу, которая находит в массиве элемент, самый близкий по величине к  данному числу. 

# В первой строке задается одно натуральное число N, не превосходящее 1000 – размер массива. 
# Во второй строке содержатся N чисел – элементы массива (целые числа, не превосходящие по модулю 1000). 
# В третьей строке вводится одно целое число x, не превосходящее по модулю 1000. 

# Вывести значение элемента массива, ближайшее к x. Если таких чисел несколько, выведите любое из них. 

# Input: 5
# 5 4 3 2 1
# 3

# Output 3

def nearest_number(arr, k):
    hm = {}
    for i in range(len(arr)):
        dif = max(arr[i] - k, k - arr[i])
        hm[i] = dif
    out = min(hm, key=hm.get)
    return arr[out]
    
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
print(nearest_number(arr, k))
