import sys

N = int(sys.stdin.readline())

ans = 0
for i in range(1,N+1):
    ans+=(N//i)*i
print(ans)