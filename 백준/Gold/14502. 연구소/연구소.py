import sys
from collections import deque #list 대신에 deque를 사용하는 것은 O(n)->O(1)시간으로 줄이기 위함임.
from copy import deepcopy #2차원 이상의 배열에서는 deepcopy 사용하기.

#Brute-force
def make_wall(count):
  if count==3:
    bfs()
    return 
  
  for i in range(N):
    for j in range(M):
      if board[i][j]==0:
        board[i][j]=1
        make_wall(count+1)
        board[i][j]=0
      
#Bfs
spread = [[1,0],[0,1],[-1,0],[0,-1]]
def bfs():
  global max_ans
  
  queue = deque()
  board_copy = deepcopy(board)
  
  for i in range(N):
    for j in range(M):
      if board_copy[i][j]==2: queue.append((i,j))
  
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x+spread[i][0], y+spread[i][1]
      if (0 <= nx < N) and (0 <= ny < M):
        if board_copy[nx][ny]==0: 
          board_copy[nx][ny]=2
          queue.append((nx,ny))
          
          
  count = 0
  for i in range(N):
    for j in range(M):
      if board_copy[i][j] == 0: count +=1
      
  max_ans = max(max_ans, count)

#Input
N,M = map(int, sys.stdin.readline().split())

board = []
for _ in range(N):
  board.append(list(map(int, sys.stdin.readline().split())))

max_ans = 0
make_wall(0)
print(max_ans)
