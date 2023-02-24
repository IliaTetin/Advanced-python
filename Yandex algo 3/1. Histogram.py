def count_occurrence(s):
    counts = {}
    for symbol in s:
        if symbol not in counts:
            counts[symbol] = 0
        counts[symbol] += 1
    max_occurrence = max(counts.values())
    return counts, max_occurrence


def build_histogram(counts, max_frequency):
    sorted_symbols = sorted(counts.keys())

    for i in range(max_frequency, 0, -1):
        for char in sorted_symbols:
            if counts[char] >= i:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print(''.join(sorted_symbols))


str_input = ''
while True:
    try:
        cur_str = input().replace(' ', '')
        str_input += cur_str
    except EOFError:
        break

occurrences, max_frequency = count_occurrence(str_input)
build_histogram(occurrences, max_frequency)
