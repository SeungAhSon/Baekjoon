import sys

def dfs():
  if len(ans) == M:
    print(*ans)
    return
  else :
    temp = 0
    for i in range(N):
      if visited[i]==0 and temp!=num_list[i]:
        visited[i]=1
        ans.append(num_list[i])
        temp = num_list[i]
        dfs()
        visited[i]=0
        ans.pop()
        
N,M = map(int, sys.stdin.readline().split())
num_list = sorted(list(map(int, sys.stdin.readline().split())))
visited = [0]*N
ans = []

dfs()
