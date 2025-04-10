N = int(input())

schedule = [list(map(int,input().split())) for i in range(N)]
dp = [0 for i in range(N+1)]

for i in range(N):
  for j in range(i+schedule[i][0],N+1):
    if dp[j]<dp[i]+schedule[i][1]:
      dp[j]=dp[i]+schedule[i][1]

print(dp[-1]) 