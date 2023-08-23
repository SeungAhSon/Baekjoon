import sys

#플루이드 워셜 풀이
N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
          if graph[i][j] or (graph[i][k] and graph[k][j]):
            graph[i][j]=1

for i in range(N):
    for j in range(N):
        print(graph[i][j], end=' ')
    print()