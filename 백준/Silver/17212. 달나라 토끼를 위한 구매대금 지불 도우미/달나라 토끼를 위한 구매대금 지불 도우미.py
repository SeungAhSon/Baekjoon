import sys

N = int(sys.stdin.readline())

dp = [i for i in range(N+1)]

for i in range(2,N+1):
    dp[i] = dp[i-1] + 1
    if i >= 2: dp[i] = min(dp[i], dp[i-2]+1)
    if i >= 5: dp[i] = min(dp[i], dp[i-5]+1)
    if i >= 7: dp[i] = min(dp[i], dp[i-7]+1)

print(dp[N])