import sys
#sys.setrecursionlimit(360000)
sys.setrecursionlimit(10**6)

movement = [[1,0],[0,1],[-1,0],[0,-1]]
def dfs(x,y):
  global max_ans
  visited[x][y]=1
  if school[x][y]=="P" : max_ans+=1

  for k in range(4):
    x_k = x + movement[k][0]
    y_k = y + movement[k][1]
    if 0<=x_k<N and 0<=y_k<M and not visited[x_k][y_k] and school[x_k][y_k]!="X": dfs(x_k, y_k)

#read input
N,M = map(int, sys.stdin.readline().split())
visited = [[0]*M for _ in range(N)]
school = []
max_ans=0

curr_x, curr_y = -1,-1
for i in range(N):
  temp = list(sys.stdin.readline().rstrip())
  if "I" in temp:  curr_x, curr_y = i, temp.index("I")
  school.append(temp)


#calculate
dfs(curr_x,curr_y)
print(max_ans if max_ans!=0 else "TT")