import sys

N = int(sys.stdin.readline())
Stairs = [int(sys.stdin.readline()) for _ in range(N)] 

dp=[0]*N
if N<=2:  print(sum(Stairs))
else :
  dp[0]=Stairs[0] 
  dp[1]=Stairs[0]+Stairs[1]
  for i in range(2,N): 
    dp[i]=max(dp[i-3]+Stairs[i-1]+Stairs[i], dp[i-2]+Stairs[i])
  print(dp[-1])