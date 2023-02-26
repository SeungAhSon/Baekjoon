def solution(rsp):
    temp = {'2':'0','0':'5','5':'2'}
    return ''.join(temp[i] for i in rsp)