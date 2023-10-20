import sys

dp = [1,1,1,2,2,3,4,5,7,9]
for i in range(10,101):
    dp.append(dp[i-1]+dp[i-5])

T = int(sys.stdin.readline())
for _ in range(T):
  N = int(sys.stdin.readline())
  print(dp[N-1])