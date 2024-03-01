import sys

R,C = map(int, sys.stdin.readline().split())

board = []
for _ in range(R):  board.append(list(sys.stdin.readline().rstrip()))


park = {0:0,1:0,2:0,3:0,4:0}
for i in range(R-1):
  count = 0
  for j in range(C-1):
    temp = [board[i][j], board[i][j+1], board[i+1][j], board[i+1][j+1]]
    if '#' in temp:   continue
    else:
      count = temp.count('X')
      park[count]+=1

for i in range(5):
  print(park[i])