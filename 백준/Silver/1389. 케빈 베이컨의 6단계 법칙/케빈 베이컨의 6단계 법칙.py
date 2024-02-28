import sys

#2644. 촌수계산 문제와 유사한 문제
def bfs(graph, start, goal):
    explored = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:  return len(new_path)-1
            explored.append(node)
    return -1
    
    
N,M = map(int, sys.stdin.readline().split())

graph = {}
for _ in range(M):
  x,y = map(int, sys.stdin.readline().split())
  if graph.get(x) is None:  graph[x]=[y]
  else:  graph[x].append(y)
  if graph.get(y) is None: graph[y]=[x]
  else: graph[y].append(x)
  
bacon = {}
for i in range(N):
  temp = 0
  for j in range(N):
    if i!=j:
      temp +=bfs(graph, i+1, j+1)
  bacon[i]=temp
print(min(bacon, key=bacon.get)+1)
