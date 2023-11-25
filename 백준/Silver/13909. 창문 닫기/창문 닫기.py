import sys
N = int(sys.stdin.readline())
ans, temp = 0, 1
while temp*temp <= N:
    temp += 1
    ans +=1
print(ans)