def solution(n):
    answer = []
    
    for i in range(2,n+1):
        while (n % i == 0):
            answer.append(i)
            n = n / i
            
    return sorted(list(set(answer)))