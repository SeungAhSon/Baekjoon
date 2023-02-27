def solution(emergency):
    temp = sorted(emergency, reverse=True)
    
    answer = []
    for i in range(len(emergency)):
        for j in range(len(temp)):
            if emergency[i]==temp[j]:
                answer.append(j+1)
    return answer