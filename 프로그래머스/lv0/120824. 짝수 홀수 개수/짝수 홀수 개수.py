def solution(num_list):
    count = 0
    for i in num_list:
        if i%2==0 : count+=1
    
    return [count, len(num_list)-count]