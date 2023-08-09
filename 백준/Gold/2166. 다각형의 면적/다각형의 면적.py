import sys

N = int(sys.stdin.readline())
x_list = []
y_list = []
for _ in range(N):
    a,b = map(int, sys.stdin.readline().split())
    x_list.append(a)
    y_list.append(b)

ans = 0
for i in range(N-1):
    ans+=x_list[i]*y_list[i+1]-x_list[i+1]*y_list[i]
ans+= x_list[-1]*y_list[0]-x_list[0]*y_list[-1]

print(round(abs(ans)/2,1))