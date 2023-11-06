import sys

n = int(sys.stdin.readline())
print(n*(n-1)*(n-2)//6) #((n-2)*(n-1)*(2*n-3)+3*(n-1)*(n-2))//12
print(3)