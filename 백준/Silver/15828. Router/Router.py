import sys
N = int(sys.stdin.readline())

stack_list = []
while True:
    temp = int(sys.stdin.readline())
    if temp == -1: break
    elif temp == 0: stack_list.pop(0)
    elif len(stack_list)>=N: pass
    else: stack_list.append(str(temp))
    

if len(stack_list)==0: print("empty")
else : print(' '.join(stack_list))