import sys

N = int(sys.stdin.readline())
A, B = map(int, sys.stdin.readline().split())

temp = A//2+B
if temp <= N: print(temp)
else : print(N)