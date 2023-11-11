import sys
sys.setrecursionlimit(100000)

def dfs(start_node):
    global temp  # Declare temp as a global variable
    temp += 1
    visited[start_node] = temp
    for i in graph[start_node]:
        if visited[i] == 0:
            dfs(i)

N, M, R = map(int, sys.stdin.readline().split())
visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]
temp = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort()

dfs(R)

# Print 0 for unreachable nodes
for i in range(1, N+1):
    print(visited[i])
