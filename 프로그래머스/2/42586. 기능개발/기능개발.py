import math

def solution(progresses, speeds):    
    N = len(progresses)
    
    #남은 작업 기간 계산
    left_days = []
    for i in range(N):
        prg, spd = progresses[i], speeds[i]
        left_days.append(math.ceil((100-prg)/spd))
    
    #리스트 추가
    answer = []
    day, cnt = left_days[0], 0
    for i in range(N):
        if left_days[i]>day:
            answer.append(cnt)
            cnt = 1
            day = left_days[i]
        else : cnt+=1 
    answer.append(cnt)
    return answer