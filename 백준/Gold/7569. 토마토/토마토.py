import sys
from collections import deque

#1012. 유기농배추랑 비슷한 문제
def dfs(n,m,h):
    dh = [0, 0, 0, 0,-1, 1]
    dn = [0, 0, 1,-1, 0, 0]
    dm = [1,-1, 0, 0, 0, 0] 
    for i in range(6):
        nh = h + dh[i]
        nn = n + dn[i]
        nm = m + dm[i]
        if (0 <= nm < M) and (0 <= nn < N) and (0 <= nh < H):
            if tomato[nh][nn][nm] == 0:
              queue.append([nn,nm,nh])
              tomato[nh][nn][nm] = tomato[h][n][m]+1

queue = deque([])
M,N,H = map(int, sys.stdin.readline().split())
tomato = []

#3차원이라 헷갈린다. 주의하기
for h in range(H):
  tomato_height = []
  for n in range(N):
    tomato_height.append(list(map(int, sys.stdin.readline().split())))
    for m in range(M):
      if tomato_height[n][m]==1:  queue.append([n,m,h])
  tomato.append(tomato_height)

while(queue):
  n,m,h = queue.popleft()
  dfs(n,m,h)

count = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m]==0:
                print(-1)
                exit(0)
        count = max(count,max(tomato[h][n]))
print(count-1)
 
 
"""
반례
input:
5 1 7
1 0 0 0 0
0 0 0 -1 0
-1 -1 0 0 0
0 0 1 -1 0
-1 -1 0 0 0
0 0 0 -1 0
1 0 0 0 0
output: 5
answer: 4
"""
