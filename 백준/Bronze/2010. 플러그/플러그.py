import sys
N = int(sys.stdin.readline())

ans = 0
for _ in range(N):
    ans += int(sys.stdin.readline())
    
print(ans-N+1)