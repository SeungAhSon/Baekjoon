import sys

#활동 선택 문제
#회의의 시작시간과 끝나는 시간이 같을 수도 있다.

N = int(sys.stdin.readline())
time_list = []
for _ in range(N):
    time_list.append(list(map(int, sys.stdin.readline().split())))
time_list.sort(key=lambda x: (x[1],x[0]))

last = 0
count = 0
for [a,b] in time_list:
    if last <= a:
        last = b
        count+=1
print(count)