def solution(dot):
    if dot[0]>0 : return 1 if dot[1]>0 else 4
    else : return 2 if dot[1]>0 else 3