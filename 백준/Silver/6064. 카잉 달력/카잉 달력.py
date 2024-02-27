import sys

def year_checker(M,N,x,y):
  k = x
  while k<=M*N:
    if (k-x)%M==0 and (k-y)%N==0:  return k
    k+=M
  return -1
    

#=============================
#Input
T = int(sys.stdin.readline())
for _ in range(T):
    M,N,x,y = map(int, sys.stdin.readline().split())
    print(year_checker(M,N,x,y))
