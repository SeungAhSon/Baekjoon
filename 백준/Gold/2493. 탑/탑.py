import sys
#stack 문제

N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

stack = []
ans = []

for i in range(N):
  while stack:
    if stack[-1][1] > sequence[i]:
      ans.append(stack[-1][0]+1)
      break
    else:
      stack.pop()
  if not stack: ans.append(0)
  stack.append([i, sequence[i]])

print(" ".join(map(str, ans)))