def solution(common):
    if common[1]-common[0] == common[-1]-common[-2]:
        return common[-1] + (common[-2]-common[-3])
    else:
        return common[-1]*(common[-2]/common[-3])
        
    return 0