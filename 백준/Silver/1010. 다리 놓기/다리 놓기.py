import sys

def fac(a):
  num = 1
  for i in range(1,a+1):	num = num*i
  return num
    
T = int(sys.stdin.readline())
for _ in range(T):
  N,M = map(int, sys.stdin.readline().split())
  #m!/((m-n)!n!)
  print(int(fac(M)/(fac(M-N)*fac(N))))