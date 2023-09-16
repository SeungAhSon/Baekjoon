import sys

T = int(sys.stdin.readline())

for i in range(T):
  N = int(sys.stdin.readline())
  temp = [j for j in range(1,N+1,2)]
  print(sum(temp))