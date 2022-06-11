#그냥 int(input())으로 받으면 시간초과가 된다.
import sys
N = int(sys.stdin.readline())

ans = 0
for _ in range(N):
    ans += int(sys.stdin.readline())
    
print(ans-N+1)
