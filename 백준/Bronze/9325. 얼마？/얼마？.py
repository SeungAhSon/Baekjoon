T = int(input())

for _ in range(T):
    S = int(input())
    N = int(input())
    
    for _ in range(N):
        Q,P = map(int, input().split())
        S+=Q*P
        
    print(S)