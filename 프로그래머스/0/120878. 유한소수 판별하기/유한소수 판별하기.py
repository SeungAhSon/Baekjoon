import math
def factorization(x):
    answer = []
    d = 2
    while d <= x:
        if x % d == 0:
            answer.append(d)
            x = x / d
        else: d = d + 1
    return set(answer)
            
def solution(a, b):
    gcd = math.gcd(a,b)
    a, b = a//gcd, b//gcd
    temp = factorization(b)
    
    return 1 if all(p==2 or p==5 for p in temp) else 2