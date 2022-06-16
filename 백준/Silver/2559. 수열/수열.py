#sum이 호출되는 횟수를 줄여야한다.
import sys
N,K = map(int, sys.stdin.readline().split())

temp = list(map(int,sys.stdin.readline().split()))
ans = [sum(temp[:K])]


for i in range(1, N-K+1):
    ans.append(ans[-1]+temp[i+K-1]-temp[i-1])
print(max(ans))
