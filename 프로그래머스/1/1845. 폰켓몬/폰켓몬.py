def solution(nums):
    #최대한 다양한 포켓몬인 N/2마리
    #최종 포켓몬의 종류만 리턴
    poke = set(nums)
    
    if len(poke)>= len(nums)//2:
        answer = len(nums)//2
    else:
        answer = len(poke)
    return answer