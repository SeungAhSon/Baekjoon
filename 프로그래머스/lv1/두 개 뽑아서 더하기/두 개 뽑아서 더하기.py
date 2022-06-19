from itertools import combinations
def solution(numbers):
    answer = list(set([sum([i,j]) for i,j in combinations(numbers,2)]))
    answer = list(set(answer)) # 중복제거
    answer.sort()
    return answer
