def dfs(node, path, cost, visited, cycle, min_cost, graph):
    if node in visited:
        if node == path[0] and cost <= min_cost:
            cycle = path
            min_cost = cost
        return cycle, min_cost
    
    visited.add(node)
    for neighbor, edge_cost in graph[node]:
        cycle, min_cost = dfs(neighbor, path+[neighbor], cost+edge_cost, visited, cycle, min_cost, graph)
    visited.remove(node)
    return cycle, min_cost

def find_least_cost_cycle(graph, nodes):
    visited = set()
    cycle = []
    min_cost = float('inf')

    for node in nodes:
        cycle, min_cost = dfs(node, [node], 0, visited, cycle, min_cost, graph)
        print(node, cycle, min_cost)

    if cycle: return cycle, min_cost
    else: return -1

T = int(input())
N,M = map(int,input().split())

graph = {}
for i in range(M):
  a,b,c = map(int,input().split())  
  if graph.get(str(a)) is None:
    graph[str(a)]=[(str(b),c)]
  else:
    graph[str(a)].append((str(b),c))


nodes = [str(i) for i in range(1,N+1)]
least_cost_cycle, least_cost = find_least_cost_cycle(graph, nodes)
print("Least cost cycle:", least_cost_cycle)
print("Cost:", least_cost)
