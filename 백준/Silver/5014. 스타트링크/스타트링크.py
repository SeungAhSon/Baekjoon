import sys
from collections import deque

#수정하기 전 코드는 66%에서 오류가 뜸.
#66% 반례 : 3 3 1 0 1
#output : 3
#answer : 2

def bfs(S):
  q = deque([S])
  
  while q:
    if S==G: return 0
    x= q.popleft()
    if x==G:  return dist[x]
    
    next_positions = [i for i in [x+U, x-D] if 0 <i<= F and i!=x and not dist[i]]
    
    for i in next_positions:
        dist[i] = dist[x]+1
        q.append(i)
        
  if dist[G] == 0: return "use the stairs"

F, S, G, U, D = map(int, sys.stdin.readline().split())
dist = [0]*(F+1)

print(bfs(S))