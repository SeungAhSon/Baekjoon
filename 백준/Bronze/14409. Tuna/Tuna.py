N = int(input())
X = int(input())

ans = 0
for _ in range(N):
    P1,P2 = map(int, input().split())
    if(abs(P1-P2)<=X) : ans += max(P1,P2)
    else : ans += int(input())
    
print(ans)