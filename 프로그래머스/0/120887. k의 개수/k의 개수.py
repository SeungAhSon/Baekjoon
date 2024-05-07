def solution(i, j, k):
    k = str(k)
    temp = list(map(str, range(i,j+1)))
    answer = ''.join(temp).count(k)
    return answer
