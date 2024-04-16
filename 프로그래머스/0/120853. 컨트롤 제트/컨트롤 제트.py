def solution(s):
    answer = []
    for i in s.split() :
        if i.lstrip("-").isdecimal() : answer.append(int(i))
        elif i=="Z" :
            if len(answer)>0 : answer = answer[:-1]
    return sum(answer)