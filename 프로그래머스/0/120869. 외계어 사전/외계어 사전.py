#spell을 모두 사용할수만 있다면 상관 없다.

def solution(spell, dic):
    len_spell = len(spell)
    for i in dic:
        count = 0
        flag = 1
        for j in spell: 
            if i.count(j)!=1: 
                flag=0
                break
        if flag : return 1
    return 2