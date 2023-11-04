import sys

a,b=map(int,sys.stdin.readline().split())
c=int(sys.stdin.readline())
n=int(sys.stdin.readline())

if a*n+b<=c*n and c>=a : print(1)
else : print(0)