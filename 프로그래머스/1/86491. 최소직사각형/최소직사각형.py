def solution(sizes):
    answer_x, answer_y = 0, 0
    for i in sizes:
        temp_x, temp_y = min(i), max(i)
        if answer_x<temp_x : answer_x  = temp_x
        if answer_y<temp_y : answer_y = temp_y
        
    return answer_x*answer_y