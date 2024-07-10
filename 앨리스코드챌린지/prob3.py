string = input()

stack = []

for char in string:
    #일단 냅다 다 넣기
    if char == ')':
        substr = ''
        while stack and stack[-1] != '(':
            substr = stack.pop() + substr
        stack.pop()

        repeat_count = int(stack.pop())
        
        expanded_length = len(substr) * repeat_count
        stack.append('x' * expanded_length)
    else:
        stack.append(char)

print(len(''.join(stack)))
