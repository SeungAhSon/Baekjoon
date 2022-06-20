N = int(input())

P = list(map(int, input().split()))
P.sort()

ans = 0
for i in range(1,N+1): ans += sum(P[0:i])
    
print(ans)