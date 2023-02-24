sequence = input().strip()

stack = []
for bracket in sequence:
    if bracket in '({[':
        stack.append(bracket)
    else:
        if not stack:
            print('no')
            break
        opening_bracket = stack.pop()
        if opening_bracket == '(' and bracket != ')':
            print('no')
            break
        elif opening_bracket == '[' and bracket != ']':
            print('no')
            break
        elif opening_bracket == '{' and bracket != '}':
            print('no')
            break
else:
    if not stack:
        print('yes')
    else:
        print('no')
