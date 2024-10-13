def count_diff(word1, word2):
    ans = 0
    for i in range(len(word1)):
        if word1[i]!=word2[i]: ans+=1
    return ans


def solution(begin, target, words):
    answer = float('inf')
    
    visited = [begin]
    
    def dfs(now, n):
        nonlocal answer
        if now==target:
            answer = min(answer, n)
            return 
        
        for word2 in words:
            if word2 not in visited and count_diff(now,word2)==1 :
                visited.append(word2)
                dfs(word2, n+1)
                visited.pop()
            
    dfs(begin, 0)
    
    return answer if answer!=float('inf') else 0

