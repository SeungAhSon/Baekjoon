import sys
import heapq

N = int(sys.stdin.readline())
heap_list = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x==0 :
        if len(heap_list)>0 : print(-1*heapq.heappop(heap_list))
        else : print(0)
    else : 
        heapq.heappush(heap_list,-1*x)