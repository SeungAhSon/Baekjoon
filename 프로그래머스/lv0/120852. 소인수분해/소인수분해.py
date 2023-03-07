def solution(n):
    answer = []
    tmp = n
    
    for i in range(2,n+1):
        while (tmp % i == 0):
            answer.append(i)
            tmp = tmp / i
            
    return sorted(list(set(answer)))