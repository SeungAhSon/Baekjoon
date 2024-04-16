def solution(num, k):
    num = list(str(num))
    return num.index(str(k))+1 if str(k) in num else -1