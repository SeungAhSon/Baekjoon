def solution(s):
    temp = []
    for i in s:
        if i=='(': temp.append(i)
        else: 
            if len(temp)==0:
                return False
            temp.pop()
    
    if len(temp)==0: return True
    else: return False