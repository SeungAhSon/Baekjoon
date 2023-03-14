def solution(s):
    temp = sorted(list(set(s)))
    s = list(s)
    
    answer = []
    for i in temp:
        if len([j for j in s if j==i])==1:
            answer.append(i)
    return ''.join(answer)