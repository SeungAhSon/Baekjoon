def solution(before, after):
    temp1 = {}
    for i in set(before):
        temp1[i] = before.count(i)

    temp2 = {}
    for i in set(after):
        temp2[i] = after.count(i)
        
    
    return 1 if temp1==temp2 else 0