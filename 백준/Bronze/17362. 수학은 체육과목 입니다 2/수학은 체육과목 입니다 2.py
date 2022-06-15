N = int(input())
ans = N%8
if ans >5 : ans = 10-ans
if ans == 0 : ans = 2
print(ans)