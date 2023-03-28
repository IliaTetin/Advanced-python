expression = input().strip().split()

stack = []
for token in expression:
    if token.isdigit():
        stack.append(int(token))
    else:
        operand2 = stack.pop()
        operand1 = stack.pop()
        if token == '+':
            result = operand1 + operand2
        elif token == '-':
            result = operand1 - operand2
        elif token == '*':
            result = operand1 * operand2
        stack.append(result)

print(stack.pop())