def solution(n, computers):
    relations = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if i!=j and computers[i][j]==1:
                relations[i].append(j)
                relations[j].append(i)
    
    visited = []
    answer = 0
    
    def dfs(i):
        if i not in visited:  visited.append(i)
        
        for j in relations[i]:
            if j not in visited: dfs(j)
        return
    
    for i in range(n):
        if i not in visited:
            dfs(i)
            answer+=1
    return answer