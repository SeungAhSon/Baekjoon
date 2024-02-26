import sys

def bfs():
  queue = [[1]]
  while queue:
    path= queue.pop(0)
    node = path[-1]
    
    if node not in explored:
        neighbours = [node+i for i in range(1,7)]

        for neighbour in neighbours:
            if neighbour in move_dict: neighbour = move_dict[neighbour]
            new_path = list(path)
            new_path.append(neighbour)
            
            queue.append(new_path)
            if neighbour >= 100:  return len(new_path)-1
        explored.append(node)
  return -1

explored = [[0 for _ in range(10)] for _ in range(10)]
dice = [1,2,3,4,5,6]

move_dict = {}
N, M = map(int, sys.stdin.readline().split())

#ladder and snake
for _ in range(N+M):
  x,y = map(int, sys.stdin.readline().split())
  move_dict[x]=y
  
print(bfs())