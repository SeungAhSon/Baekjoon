def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit(): answer.append(int(i))
    return sum(answer)