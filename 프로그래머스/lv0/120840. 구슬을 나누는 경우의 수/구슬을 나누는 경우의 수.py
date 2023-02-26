def fact(n):
    ans = 1
    for i in range(2,n+1): ans*=i
    return ans

def solution(balls, share):
    return fact(balls)/(fact(balls-share)*fact(share))