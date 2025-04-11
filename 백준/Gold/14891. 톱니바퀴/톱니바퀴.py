wheel = [list(map(int, input().strip())) for _ in range(4)]
K = int(input())
action = [tuple(map(int, input().split())) for _ in range(K)]

def turn_wheel(arr, d):
    if d==1:
        arr = [arr[-1]] + arr[:-1]
    else:
        arr = arr[1:] + [arr[0]]
    return arr

for a,b in action:
    a -=1

    dir = [0] * 4
    dir[a] = b

    #left
    for i in range(a-1, -1,-1):
        if wheel[i][2] != wheel[i+1][6]:
            dir[i] = -dir[i+1]

    #right
    for i in range(a+1, 4):
        if wheel[i-1][2] != wheel[i][6]:
            dir[i] = -dir[i-1]

    for i in range(4):
        if dir[i]!=0:
            wheel[i] = turn_wheel(wheel[i], dir[i])

ans = 0
for i in range(4):
    ans += (wheel[i][0]==1)*(2**i)
print(ans)