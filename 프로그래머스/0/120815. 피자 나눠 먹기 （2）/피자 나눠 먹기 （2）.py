def solution(n):
    for i in range(min(n,6),n*6+1):
        if i%6==0 and i%n==0:
            return i/6