import sys
#python의 deep copy, shallow copy

N = int(sys.stdin.readline())
    
dp = [[0,1,1,1,1,1,1,1,1,1]]+[[[0] for _ in range(10)] for __ in range(N-1)]

for i in range(1, N):
    for j in range(10):
        if j==0:  dp[i][j] = dp[i-1][1]
        elif 1<=j<=8 : dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] 
        else: dp[i][j] = dp[i-1][8]
        
print(sum(dp[N-1]) % 1000000000)