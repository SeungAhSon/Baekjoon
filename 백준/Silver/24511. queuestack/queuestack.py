import sys
from collections import deque
#문제에 주어진대로 그대로 구현하면 시간초과과 됨
#스택이 의미가 있는지

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split())) # 0=queue, 1=stack
B = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))

queuestack = deque()
for i in range(N):
  if A[i]==0: queuestack.appendleft(B[i])


ans = []
for i in range(M):
  queuestack.append(C[i])
  temp = queuestack.popleft()
  
  ans.append(str(temp))
    
print(" ".join(ans))