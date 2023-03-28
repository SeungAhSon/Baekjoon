def solution(lines):
    table = [0]*200
    
    for line in lines:
        a,b = line
        for i in range(a,b): table[i]+=1
        
    count = 0
    for i in range(200):
        if table[i]>1: count += 1

    return count