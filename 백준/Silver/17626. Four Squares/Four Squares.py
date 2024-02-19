import sys
#Dynamic program 문제
#나중에 한번 더 보자

N = int(sys.stdin.readline())
dp = [i for i in range(N+1)] 

for i in range(2,N+1):
  for j in range(1, i+1):
    temp = j**2
    if temp>i: break
    #제곱수로 표현할 때 가장 항의 개수가 작은 j 를 찾기
    if dp[i] > dp[i - temp] + 1:  dp[i] = dp[i - temp] + 1
print(dp[N])