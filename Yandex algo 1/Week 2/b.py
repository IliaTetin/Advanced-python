# По последовательности чисел во входных данных определите ее вид:

#    CONSTANT – последовательность состоит из одинаковых значений
#    ASCENDING – последовательность является строго возрастающей
#    WEAKLY ASCENDING – последовательность является нестрого возрастающей
#    DESCENDING – последовательность является строго убывающей
#    WEAKLY DESCENDING – последовательность является нестрого убывающей
#    RANDOM – последовательность не принадлежит ни к одному из вышеупомянутых типов

# Формат ввода 
# По одному на строке поступают числа последовательности ai, |ai| ≤ 109.
# Признаком окончания последовательности является число -2× 109. Оно в последовательность не входит.

# Формат вывода
# В единственной строке выведите тип последовательности.

# Input
# 530
# -530
# -2000000000

#Output: CONSTANT

prev = int(input())
out = None

while True:
    cur = int(input())
    if cur == -2000000000:
        break
    if cur == prev:
        if out == 'ASCENDING':
            out = 'WEAKLY ASCENDING'
        elif out == 'DESCENDING':
            out = 'WEAKLY DESCENDING'
        elif out == None:
            out = 'CONSTANT'
    elif (cur > prev) and (out == None):
        out = 'ASCENDING'
    elif (cur > prev) and (out == 'CONSTANT'):
        out = 'WEAKLY ASCENDING'
    elif (cur > prev) and (out == 'DESCENDING' or out == 'WEAKLY DESCENDING'):
        out = 'RANDOM'
    elif (cur < prev) and (out == None): 
        out = 'DESCENDING'
    elif (cur < prev) and (out == 'CONSTANT'):
        out = 'WEAKLY DESCENDING'
    elif (cur < prev) and (out == 'ASCENDING' or out == 'WEAKLY ASCENDING'):
        out = 'RANDOM'
    prev = cur
print(out)