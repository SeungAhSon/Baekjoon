N = int(input())
M = int(input())

computer = [[0]*(N+1) for i in range(N+1)]
visited = [0]*(N+1)


for _ in range(M):
    a,b = map(int,input().split())
    computer[a][b] = 1
    computer[b][a] = 1
    

def dfs(node):
    visited[node]=1
    for i in range(1,N+1):
        if (computer[node][i]==1) and (visited[i]==0):
            visited[i]=1
            dfs(i)
    return visited.count(1)-1

print(dfs(1))