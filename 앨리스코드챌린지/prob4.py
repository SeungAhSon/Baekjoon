from collections import defaultdict, deque

#===input===
tree = defaultdict(list)
N = int(input())

for _ in range(N-1):
  u,v = map(int, input().split())
  tree[u].append(v)
  tree[v].append(u)


stack = []
queue = deque([1])
visited = [False] * (N + 1)
visited[1] = True

while queue:
    node = queue.popleft()
    stack.append(node)
    for child in tree[node]:
        if not visited[child]:
            visited[child] = True
            queue.append(child)
print(stack)
#=============================
visited = [False] * (N + 1)
diff = [0] * (N + 1)

while stack:
  node = stack.pop()
  visited[node] = True
  isLeaf = True

  min_child = float('inf')
  for j in tree[node]:
    if visited[j]:
      isLeaf = False
      min_child = min(min_child, diff[j])
  if isLeaf: diff[node]=node
  else: diff[node] = node-min_child
    
for i in range(1, N+1):
  if diff[i]>=0: print(1)
  else: print(0)
