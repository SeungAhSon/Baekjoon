def solution(array, n):
    temp = sorted([abs(i-n) for i in array]) 
    
    return n-temp[0] if n-temp[0] in array else n+temp[0]