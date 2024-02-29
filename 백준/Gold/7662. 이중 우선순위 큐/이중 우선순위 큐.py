import sys
import heapq

#max, min로 쌩 구현하면 시간초과가 난다.
#우선순위 큐로 정렬해서 보관하도록 한다.
# heapq는 최대힙을 지원안하기에 구현해야한다.

T = int(sys.stdin.readline())

for _ in range(T):
  max_Queue, min_Queue = [], []
  k = int(sys.stdin.readline())
  visited = [0]*k
  
  for i in range(k):
    A,B = sys.stdin.readline().rstrip().split()
    B = int(B)
    
    if A=='I':
      heapq.heappush(min_Queue, (B,i))
      heapq.heappush(max_Queue, (-B,i))
      visited[i]=1
    else:
      if len(min_Queue)>0:
        if B==-1:
          while min_Queue:
            temp = heapq.heappop(min_Queue)
            if visited[temp[1]]==1 :
              visited[temp[1]]=0
              break
          
        else :
          while max_Queue:
            temp = heapq.heappop(max_Queue)
            if visited[temp[1]]==1 :
              visited[temp[1]]=0
              break
  while min_Queue and not visited[min_Queue[0][1]]:
    heapq.heappop(min_Queue)
  while max_Queue and not visited[max_Queue[0][1]]:
    heapq.heappop(max_Queue)
    
  if max_Queue and min_Queue: print(-max_Queue[0][0], min_Queue[0][0]) 
  else : print("EMPTY")
      
      