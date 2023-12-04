import sys

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
    
    
N = int(sys.stdin.readline())
A, B = sys.stdin.readline().rstrip().split()
M = int(sys.stdin.readline())

graph = {}
visited = [0]*(N+1)

for _ in range(M):
  x, y = sys.stdin.readline().rstrip().split()
  if graph.get(x) is None:  graph[x]=[y]
  else:  graph[x].append(y)
    
  if graph.get(y) is None: graph[y]=[x]
  else: graph[y].append(x)

print(bfs(graph, A, B))