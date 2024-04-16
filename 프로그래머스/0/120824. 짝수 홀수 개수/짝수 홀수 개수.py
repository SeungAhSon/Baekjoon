def solution(num_list):
    answer = [0,0]
    for i in num_list: answer[i%2]+=1
    return answer