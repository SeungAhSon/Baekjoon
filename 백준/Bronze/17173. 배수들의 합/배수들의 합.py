import sys

N,M = map(int, sys.stdin.readline().split())
K = list(map(int, sys.stdin.readline().split()))

ans = 0
for i in range(1,N+1):
  for j in K:
    if i%j==0:
      ans+=i
      break

print(ans)