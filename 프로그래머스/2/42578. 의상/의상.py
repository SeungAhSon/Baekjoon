def solution(clothes):
    temp_dict = {}
    
    for i,j in clothes:
        if j in temp_dict: temp_dict[j].append(i)
        else: temp_dict[j] = [i]
    
    answer = 1
    for i in temp_dict:
        print(i)
        answer*=(len(temp_dict[i])+1)
        
    return answer-1