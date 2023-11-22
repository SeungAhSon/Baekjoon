import sys

N = int(sys.stdin.readline())
stud = list(map(int,sys.stdin.readline().split()))
stack = []
target = 1

while len(stud) or len(stack) or target<N+1:
  if stud and stud[0]==target:
    stud.pop(0)
    target+=1
  elif stack and stack[-1]==target:
    stack.pop(-1)
    target+=1
  else:
    if len(stud):  stack.append(stud.pop(0))
    else: break
    
if len(stud)!=0 or len(stack)!=0: print("Sad")
else :print("Nice")