def solution(num):
    
    #테스트 13 : input이 1일떄 return 0
    if(num==1) : return 0

    ans = 0
    for i in range(500):
        num = num//2 if num%2==0 else num*3+1
        ans += 1 
        if num==1 : break
        if(num!=1 and ans>=500):
            ans = -1
            break
        
    return ans
