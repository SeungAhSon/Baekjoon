import sys
N = int(sys.stdin.readline())

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    print((a+b)*(a+b-1)*(a+b)//2)