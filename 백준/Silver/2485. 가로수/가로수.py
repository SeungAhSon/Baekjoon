import sys
import math
            
N = int(sys.stdin.readline())
temp = int(sys.stdin.readline())

diff = []
for i in range(N-1):
    x = int(sys.stdin.readline())
    diff.append(x-temp)
    temp = x

gcd = diff[0]
for i in range(1, len(diff)):
    gcd = math.gcd(gcd, diff[i])

ans = 0
for i in diff:  ans+= i//gcd-1
print(ans)