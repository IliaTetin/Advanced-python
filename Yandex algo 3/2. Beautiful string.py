ALPHABET_LENGTH = 26
FIRST_SYMBOL_ASCII = ord('a')

def find_max_beauty(substitution_count, string):
    symbol_counts = [0] * ALPHABET_LENGTH
    start = end = 0
    max_count = 0
    while end < len(string):
        symbol_counts[ord(string[end]) - FIRST_SYMBOL_ASCII] += 1
        max_frequency = max(symbol_counts)
        
        if end - start + 1 - max_frequency > substitution_count:
            symbol_counts[ord(string[start]) - FIRST_SYMBOL_ASCII] -= 1
            start += 1
        
        max_count = max(max_count, end - start + 1)
        end += 1

    return max_count

substitution_n = int(input())
string_input = input().strip()

max_beauty = find_max_beauty(substitution_n, string_input)
print(max_beauty)
