def solution(keyinput, board):
    x,y=0,0
    for i in keyinput:
        if i=="up": y=min(y+1,board[1]//2)
        elif i=="down": y=max(-(board[1]//2),y-1)
        elif i=="left": x=max(-(board[0]//2),x-1)
        elif i=="right": x=min(x+1,board[0]//2)
    return [x,y]