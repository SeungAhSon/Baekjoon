import sys
import heapq
from collections import defaultdict

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

#graph 입력받기
graph = defaultdict(list)
for _ in range(M):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

#start, end 입력받기
start, end = map(int, sys.stdin.readline().split())
prev_node = [0]*(N+1)
distance = [10e9]*(N+1)

#다익스트라 알고리즘 - 지희선배 코드 참고
def dikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                prev_node[i[0]] = now
                heapq.heappush(q, (cost, i[0]))
                
dikstra(start)

path = [end]
now = end
while now!=start:
    now = prev_node[now]
    path.append(now)
path.reverse()

#결과 출력
print(distance[end])
print(len(path))
print(" ".join(map(str,path)))