def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board)):
            temp = board[i][j]
            if i!=0 and j!=0: temp += board[i-1][j-1]
            if i!=0: temp += board[i-1][j]
            if i!=0 and j!=len(board)-1 : temp+=board[i-1][j+1]
            if i!=len(board)-1 : temp+=board[i+1][j]
            
            if j!=0: temp+=board[i][j-1]
            if j!=len(board)-1 : temp += board[i][j+1]
            if i!=len(board)-1 and j!=0: temp += board[i+1][j-1]
            if i!=len(board)-1 and j!=len(board)-1: temp += board[i+1][j+1]
            if temp==0:
                answer+=1
    return answer

