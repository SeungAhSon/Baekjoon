import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
  temp = sys.stdin.readline().split()
  if temp[0]=='1': stack.append(temp[1]) 
  elif temp[0]=='2': print(stack.pop() if stack else -1)
  elif temp[0]=='3': print(len(stack))
  elif temp[0]=='4': print(1 if not stack else 0)
  elif temp[0]=='5': print(stack[-1] if stack else -1)