import sys

N = int(sys.stdin.readline())
paper = []

for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().strip().split())))

white = 0
blue = 0

def cut(x,y,N):
    global white
    global blue

    color = paper[x][y]
    same_flag = True
    for i in range(x,x+N):
        for j in range(y,y+N):
            if color != paper[i][j]:
                same_flag = False
                break
    if same_flag : #0->white, 1->blue
        if color==0 : white += 1
        else :blue += 1
    else :
        cut(x, y, N//2)
        cut(x, y+N//2, N//2)
        cut(x+N//2, y, N//2)
        cut(x+N//2, y+N//2, N//2)

cut(0,0,N)
print(white)
print(blue)