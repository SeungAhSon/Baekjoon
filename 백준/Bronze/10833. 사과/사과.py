N = int(input())

ans = 0
for _ in range(N):
    A,B = map(int, input().split())
    ans += B%A
    
print(ans)