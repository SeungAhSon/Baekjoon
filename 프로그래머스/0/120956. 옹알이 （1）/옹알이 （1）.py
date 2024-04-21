def solution(babbling):
    bab = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in babbling:
        while len(i)>1:
            if i[:2] == "ye" or i[:2] == "ma": i = i[2:]
            elif i[:3] == "aya" or i[:3] == "woo": i = i[3:]
            else : break
        if len(i)==0: answer+=1
        
    return answer