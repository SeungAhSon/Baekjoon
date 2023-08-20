import sys

N = int(sys.stdin.readline())
ans = 1
for i in range(2,N+1):
    ans*=i
print(ans)