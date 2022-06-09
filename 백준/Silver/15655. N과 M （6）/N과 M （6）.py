N, M = map(int,input().split())
L = list(map(int,input().split()))
L.sort()

ans = []
def dfs(count):
    if len(ans)==M:
        print(' '.join(map(str,ans)))
        return
    
    for i in range(count,N):
        if L[i] not in ans :
            ans.append(L[i])
            dfs(i+1)
            ans.pop()

dfs(0)