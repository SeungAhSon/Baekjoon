def solution(s):
    num = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    for i in num.items():
        s = s.replace(i[0], str(i[1])) 
    
    return int(s)