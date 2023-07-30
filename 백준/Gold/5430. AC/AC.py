import sys
from collections import deque

#list reverse를 사용하면 timeout

T = int(sys.stdin.readline())

for _ in range(T):
    req = sys.stdin.readline()
    N = int(sys.stdin.readline())

    if N==0:
        arr = sys.stdin.readline()
        if "D" in req : print("error")
        else : print("[]")
    else :
        arr = deque(sys.stdin.readline()[1:-2].split(','))
        rev_flag = False
        for i in req:
            if i=="R" : rev_flag = not rev_flag
            elif i=="D" : 
                if arr :
                    if rev_flag : arr.pop()
                    else : arr.popleft()
                else : 
                    print("error")
                    arr = []
                    break
        if arr!=[] :
            if rev_flag : arr.reverse()
            print("["+",".join(arr)+"]")