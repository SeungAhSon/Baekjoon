
from collections import deque

N,M,K = map(int, input().split())
Table = [list(map(int, input().split())) for _ in range(N)]
Count = [[-1 for i in range(M)] for j in range(N)]

def select_Attacker():
    position = []
    for i in range(N):
        for j in range(M):
            if Table[i][j]!=0:
                position.append([i,j,Table[i][j], Count[i][j], i+j, j])
    position.sort(key=lambda x: (x[2], -x[3], -x[4], -x[5]))
    return position[0][0], position[0][1]

def select_Victim():
    position = []
    for i in range(N):
        for j in range(M):
            if Table[i][j]!=0:
                position.append([i,j,Table[i][j], Count[i][j], i+j, j])
    position.sort(key=lambda x: (-x[2], x[3], x[4], x[5]))
    return position[0][0], position[0][1]

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def Laser(r1,c1,r2,c2):
    queue = deque([(r1,c1, [])])
    visited = [[0 for i in range(M)] for j in range(M)]
    for i in range(N):
        for j in range(M):
            if Table[i][j]==0: visited[i][j]=1
    while queue:
        curr_x, curr_y, path = queue.popleft()
        if (curr_x, curr_y) == (r2,c2): return path
        for dx,dy in dir:
            new_x = (curr_x+dx)%N
            new_y = (curr_y+dy)%M
            if visited[new_x][new_y]==0:
                visited[new_x][new_y]=2
                queue.append((new_x, new_y, path + [(new_x, new_y)]))

    return []

def Attack(r1,c1,r2,c2):
    # 레이저 공격
    path = Laser(r1,c1, r2, c2)

    # 포탄 공격
    if path==[]:
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                r = (r2+i)%N
                c = (c2+j)%M
                path.append((r, c))

    # 실제 공격
    for r,c in path:
        if r==r2 and c==c2:
            Table[r2][c2] -= Table[r1][c1]
        else:
            Table[r][c] -= Table[r1][c1]//2

    return path

#main
for i in range(K):

    # 1. 공격자 선정
    r1,c1 = select_Attacker()

    # 2. 공격자의 공격
    r2,c2 = select_Victim()

    Table[r1][c1] += N+M
    Count[r1][c1] = i

    path = Attack(r1,c1, r2, c2)

    # 3. 포탑 부서짐
    cnt = 0
    for i in range(N):
        for j in range(M):
            if Table[i][j]<0:
                Table[i][j] = 0
            elif Table[i][j]>0:
                cnt+=1
    if cnt==1:
        break

    # 4. 포탑 정비
    for i in range(N):
        for j in range(M):
            if Table[i][j] > 0 and (i, j) != (r1, c1) and (i, j) not in path:
                Table[i][j] += 1


# 가장 강한 포탑
ans = 0
for i in range(N):
    for j in range(M):
        if Table[i][j] > ans:
            ans = Table[i][j]
print(ans)