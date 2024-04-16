def solution(n):
    temp = 1
    while n>0:
        if (temp//10!=3 and temp//10!=13) and (temp%10!=3) and temp%3!=0:
            n-=1
        temp+=1
        
    return temp-1