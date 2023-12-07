import sys
import math

K = int(sys.stdin.readline())
ans = []


#소인수분해
for i in range(2, math.ceil(K**(1/2))+1):
    while K%i == 0:
        ans.append(i)
        K//=i
if K != 1: ans.append(K)
print(len(ans))
print(*ans)
