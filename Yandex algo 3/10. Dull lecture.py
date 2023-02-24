s = input()

char_count = {}
for i, char in enumerate(s):
    char_count[char] = char_count.get(char, 0) + (i + 1) * (len(s) - i)

result = []
for char, count in sorted(char_count.items()):
    result.append(f"{char}: {count}")

print("\n".join(result))
