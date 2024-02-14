import sys

movement = [[-1,0],[1,0],[0,-1],[0,1]]
#dfs
def search1(x,y,count, temp):
  global max_ans
  if count==3:  max_ans = max(max_ans, temp)
  else:
    for i in range(4):
      nx = x+movement[i][0]
      ny = y+movement[i][1]
      if 0<=nx<N and 0<=ny<M:
        if visit[nx][ny] == 0 :
          visit[nx][ny] = 1
          search1(nx,ny,count+1,temp+paper[nx][ny])
          visit[nx][ny] = 0

#凸모양 탐색
def search2(x,y, temp):
  global max_ans
  count = 0
  
  for k in range(4):
    nx = x+ movement[k][0]
    ny = y+ movement[k][1]
    if 0<=nx<N and 0<=ny<M: 
      temp += paper[nx][ny]
      count += 1

  if count==3 :  max_ans = max(max_ans, temp)
  elif count==4 :
    for k in range(4):
      nx = x+ movement[k][0]
      ny = y+ movement[k][1]
      max_ans = max(max_ans, temp- paper[nx][ny])

#====================================
#Input
N, M = map(int, sys.stdin.readline().split())
visit = [[0 for _ in range(M)] for _ in range(N)]
paper = []
for _ in range(N):
  paper.append(list(map(int, sys.stdin.readline().split())))
  
#====================================
#Search
max_ans = 0

for i in range(N):
  for j in range(M):
    visit[i][j] = 1
    search1(i,j,0, paper[i][j])
    search2(i,j, paper[i][j])
    visit[i][j] = 0
print(max_ans)
