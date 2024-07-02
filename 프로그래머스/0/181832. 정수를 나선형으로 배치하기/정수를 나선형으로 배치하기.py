move = [[1,0],[0,1],[-1,0],[0,-1]]

def solution(n):
    answer = [[0] * n for _ in range(n)]
    x, y, curr = 0, 0, 1
    while n>0:
        answer[y][x] = curr
        
        for i in range(4):
            for _ in range(n-1):
                answer[y][x] = curr
                x, y = x+move[i][0], y+move[i][1]
                curr+=1
        n -= 2
        x,y = x+1, y+1
    return answer