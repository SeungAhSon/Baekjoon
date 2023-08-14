import sys

N, m, M, T, R= map(float,sys.stdin.readline().split())

total_time = 0
ex_time = 0
beat = m
while ex_time<N:
    if m+T>M:
        break
    if beat+T<=M:
        beat += T
        ex_time += 1
    else : 
        beat = max(beat-R,m)
    total_time+=1

print(total_time if ex_time==N else -1)