import sys
sys.setrecursionlimit(10000)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def dfs(x, y):
  visited[x][y]=1
  current_color = color_field[x][y]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if (0 <= nx < N) and (0 <= ny < N):
      if visited[nx][ny]==False:
        if color_field[nx][ny] == current_color:
          dfs(nx,ny)

#Input
N = int(sys.stdin.readline())
color_field = []

for _ in range(N):
  temp = sys.stdin.readline().rstrip()
  color_field.append(list(temp))
    
#Calculate - (1) non-color blind
non_count = 0
visited = [[0 for _ in range(N)] for _ in range(N)]
for x in range(N):
  for y in range(N):
    if visited[x][y] == 0:
      dfs(x, y)
      non_count+=1

#change G to R
for x in range(N):
  for y in range(N):
    if color_field[y][x] == "G": color_field[y][x] = "R"

#Calculate - (2) color blind
blind_count = 0
visited = [[0 for _ in range(N)] for _ in range(N)]
for x in range(N):
  for y in range(N):
    if visited[x][y] == 0:
      dfs(x, y)
      blind_count+=1
        
print(non_count, blind_count)