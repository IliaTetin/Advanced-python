# Решите в целых числах уравнение:
# math.sqrt(ax + b) = c
# a, b, c – данные целые числа: найдите все решения или сообщите, что решений в целых числах нет.

# Программа должна вывести все решения уравнения в порядке возрастания, либо NO SOLUTION (заглавными буквами), если решений нет. Если решений бесконечно много, вывести MANY SOLUTIONS. 

# Input 1 0 0
# Output 0

def Week1_d(a,b,c):
    if a == 0 and b == 0 and c == 0:
        return 'MANY SOLUTIONS'
    if c < 0:
        return 'NO SOLUTION'
    if a == 0 and b ** 0.5 == c:
        return 'MANY SOLUTIONS'
    if a == 0:
        return 'NO SOLUTION'
    res = (c ** 2 - b) / a
    if int(res) == res:
        return int(res)
    else:
        return 'NO SOLUTION'

a = int(input())
b = int(input())
c = int(input()) 
print(Week1_d(a,b,c))