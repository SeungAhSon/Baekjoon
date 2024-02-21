import sys
from collections import deque

def bfs(A,B):
  visited = [0] * 10000
  visited[A] = 1
  Queue = deque([(A,'')])

  while Queue:
    A_temp, ans = Queue.popleft()
    if A_temp==B:  return ans
  
    if not visited[2*A_temp%10000]: #D
      visited[2*A_temp%10000]=1
      Queue.append((2*A_temp%10000, ans+'D'))
  
    if not visited[(A_temp-1) % 10000]: #S
      visited[(A_temp-1) % 10000]=1
      Queue.append(((A_temp-1) % 10000, ans+'S'))
    
    if not visited[A_temp%1000*10+A_temp//1000]: #L
      visited[A_temp%1000*10+A_temp//1000]=1
      Queue.append((A_temp%1000*10+A_temp//1000, ans+'L'))
    
    if not visited[int(A_temp%10*1000+A_temp//10)]: #R
      visited[A_temp%10*1000+A_temp//10]=1
      Queue.append((A_temp%10*1000+A_temp//10, ans+'R'))

#===================================
movement = ['D','S','L','R']
T = int(sys.stdin.readline())

for _ in range(T):
  A, B = map(int, sys.stdin.readline().split())
  print(bfs(A,B))