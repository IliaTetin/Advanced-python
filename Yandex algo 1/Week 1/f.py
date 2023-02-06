# В школе решили на один прямоугольный стол поставить два прямоугольных ноутбука. 
# Ноутбуки нужно поставить так, чтобы их стороны были параллельны сторонам стола. 
# Определите, какие размеры должен иметь стол, чтобы оба ноутбука на него поместились, и площадь стола была минимальна.

# Вводится четыре натуральных числа, первые два задают размеры одного ноутбука, а следующие два — размеры второго. Числа не превышают 1000.

# Выведите два числа — размеры стола. Если возможно несколько ответов, выведите любой из них (но только один).

# Input
# 10 2 2 10
# Output
# 20 2
# 2 20
# 4 10
# 10 4

# В примерах указаны всевозможные ответы на поставленную задачу. Ваша программа должна вывести один из них. 

def Week1_f(xt, yt, xn, yn):
    options = [
        (xt + xn, max(yt, yn)),
        (xt + yn, max(yt, xn)),
        (yt + yn, max(xt, xn)),
        (yt + xn, max(xt, yn))
    ]
    return min(options, key=lambda x: x[0] * x[1])

xt, yt, xn, yn = map(int, input().split())
print(*Week1_f(xt, yt, xn, yn))
    