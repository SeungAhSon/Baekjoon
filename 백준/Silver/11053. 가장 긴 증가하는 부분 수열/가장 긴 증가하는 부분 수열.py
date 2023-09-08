import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

dp = [0]*N
dp[0] = 1;

for i in range(1,N):
  dp[i]=1
  for j in range(0,i):
    if num_list[i]>num_list[j]: dp[i]=max(dp[i],dp[j]+1)
    
print(max(dp))