def solution(numbers, direction):
    if direction=="left" : return numbers[1:]+[numbers[0]]
    else : return [numbers[-1]]+numbers[:-1]