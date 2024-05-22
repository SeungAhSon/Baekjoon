import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
lantern = list(map(int, sys.stdin.readline().split()))
last = ans = lantern[0]

for i in range(M):
    temp = abs(last-lantern[i])
    temp = temp//2 if temp % 2 == 0 else (temp//2) + 1  

    ans = max(ans, temp)
    last = lantern[i]

ans = max(ans, abs(N-lantern[len(lantern)-1]))
print(ans)