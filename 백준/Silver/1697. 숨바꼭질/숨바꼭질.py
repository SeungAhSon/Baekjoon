import sys
from collections import deque
def bfs(x):
  q = deque([x])
  while q:
    x= q.popleft()
    if x==K:  return dist[x]
    
    for i in [x-1,x+1,2*x]:
      if 0<=i and i<=MAX and not dist[i]:
        dist[i] = dist[x]+1
        q.append(i)

MAX = 10**5
dist = [0]*(MAX+5)
N,K = map(int, sys.stdin.readline().split())
print(bfs(N))
