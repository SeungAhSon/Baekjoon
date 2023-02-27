def solution(n):
    answer = 1
    for i in range(1, n//2+1):
        if n%i==0 : answer+=1
    
    return answer