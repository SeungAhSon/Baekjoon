import sys

N, M = map(int, sys.stdin.readline().split())
basket = [i for i in range(1,N+1)]

for _ in range(M):
  i, j = map(int, sys.stdin.readline().split())
  temp = basket[j-1]
  basket[j-1] = basket[i-1]
  basket[i-1] = temp
  
print(' '.join(map(str, basket)))