import sys

N = int(sys.stdin.readline())
chick = list(map(int, sys.stdin.readline().split()))
ans = 0

for i in range(3) :
    if chick[i] <= N :  ans += chick[i]
    else :  ans += N

print(ans)