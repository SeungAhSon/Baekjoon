def solution(numbers, target):
    answer = 0
    
    def dfs(x, n = 0) :
        nonlocal answer
        
        if len(numbers)==n:
            if x==target:
                answer+=1
            return
        
        dfs(x+numbers[n], n+1)
        dfs(x-numbers[n], n+1)
        
    dfs(0, 0)

    return answer