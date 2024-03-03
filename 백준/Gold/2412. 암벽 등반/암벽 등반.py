import sys
from collections import deque

def bfs():
  Queue = deque([[0,0,0]])
  while Queue:
    x, y, ans = Queue.popleft()
    if y==T: return ans
    
    for i in range(-2,3):
      for j in range(-2,3):
        x_temp, y_temp = x+i, y+j
        if (x_temp,y_temp) in board:
          Queue.append([x_temp, y_temp, ans+1])
          board.remove((x_temp, y_temp))
  return -1
  
  
#Input
N,T = map(int, sys.stdin.readline().split())
visited = [0]*N
board = set()
for _ in range(N):
  x,y = map(int, sys.stdin.readline().split())
  board.add((x,y))

print(bfs())