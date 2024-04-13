def solution(priorities, location):
    #우선순위와 위치를 저장하는 리스트
    loc_pri = []
    for i in range(len(priorities)):
        loc_pri.append((priorities[i], i))
    
    #계산
    ans = 1
    while len(loc_pri)>1:
        temp = loc_pri.pop(0)
        if temp[0]<max(a for a,_ in loc_pri):
            loc_pri.append(temp)
            
        else:
            if temp[1]==location: return ans
            ans+=1
    
    return ans