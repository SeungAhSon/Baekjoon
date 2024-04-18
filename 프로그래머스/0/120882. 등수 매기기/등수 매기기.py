def solution(score):
    temp = [(i+1, sum(score[i])) for i in range(len(score))]
    temp.sort(key=lambda x: x[1], reverse=True)
    
    current_rank = 1
    answer = [(temp[0][0], 1)]
    
    for i in range(1,len(temp)):
        if temp[i-1][1]!=temp[i][1]: current_rank = i+1
        answer.append((temp[i][0], current_rank))
    answer.sort(key=lambda x: x[0])    
    
    return [i[1] for i in answer]
