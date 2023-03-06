def solution(n):
    ans = 1
    tmp = 1
    while tmp<=n:
        ans+=1
        tmp*=ans
    return ans-1