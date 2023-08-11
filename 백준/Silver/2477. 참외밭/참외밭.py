import sys

#2166 다각형의 면적과 유사한 문제
#https://www.acmicpc.net/problem/2166

K = int(sys.stdin.readline())

x_list, y_list = [], []
curr_x, curr_y = 0, 0

for _ in range(6):
    a,b = map(int, sys.stdin.readline().split())
    if a==1: curr_x += b
    elif a==2: curr_x -= b
    elif a==3: curr_y -= b
    elif a==4: curr_y += b

    x_list.append(curr_x)
    y_list.append(curr_y)

ans = 0
for i in range(5):
    ans+=x_list[i]*y_list[i+1]-x_list[i+1]*y_list[i]
ans+= x_list[-1]*y_list[0]-x_list[0]*y_list[-1]

print(K*ans//2)