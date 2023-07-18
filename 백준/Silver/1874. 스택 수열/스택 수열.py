import sys

n = int(sys.stdin.readline())
sequence = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
result = []
current_num = 1

for i in sequence:
    while current_num <= i:
        stack.append(current_num)
        result.append('+')
        current_num += 1
    if stack[-1] == i:
        stack.pop()
        result.append('-')
    else:
        result = ["NO"]
        break
        
for op in result:
    print(op)