import sys

N = int(sys.stdin.readline())
for i in range(1,N+1):
    num = list(map(int, sys.stdin.readline().split()))
    num.sort()
    
    if num[0]+num[1]<=num[2]:
        print(f"Case #{i}: invalid!")
    elif num[0]==num[1]==num[2]:
        print(f"Case #{i}: equilateral")
    elif num[0]==num[1] or num[1]==num[2] or num[0]==num[2]:
        print(f"Case #{i}: isosceles")
    else:
        print(f"Case #{i}: scalene")