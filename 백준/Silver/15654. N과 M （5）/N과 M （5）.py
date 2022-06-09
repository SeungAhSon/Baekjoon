N, M = map(int, input().split())
L = list(map(int, input().split()))
L.sort()

ans = []
def dfs():
    if len(ans)==M:
        print(' '.join(map(str,ans)))
        return
    
    for i in L:
        if i not in ans:
            ans.append(i)
            dfs()
            ans.pop()

dfs()