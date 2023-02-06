# За многие годы заточения узник замка Иф проделал в стене прямоугольное отверстие размером D × E. Замок Иф сложен из кирпичей, размером A × B × C. Определите, сможет ли узник выбрасывать кирпичи в море через это отверстие, если стороны кирпича должны быть параллельны сторонам отверстия.
# Формат ввода
# Программа получает на вход числа A, B, C, D, E.
# Формат вывода
# Программа должна вывести слово YES или NO.

def uznik(brick, window):
    window.sort()
    brick.sort()
    if brick[0] <= window[0] and brick[1] <= window[1]:
        return 'YES'
    else:
        return 'NO'



brick = [None, None, None]
window = [None, None]
brick[0] = int(input())
brick[1] = int(input())
brick[2] = int(input())
window[0] = int(input())
window[1] = int(input())
print(uznik(brick, window))
