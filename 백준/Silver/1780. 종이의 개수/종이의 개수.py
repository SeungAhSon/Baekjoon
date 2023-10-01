import sys

N = int(sys.stdin.readline())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

ans1, ans2, ans3 = 0,0,0

def reccu(N,a,b):
  global ans1, ans2, ans3
  first_element = matrix[a][b]
  for i in range(a,a+N):
    for j in range(b,b+N):
      if matrix[i][j] != first_element:
        for x in range(3):
          for y in range(3):
            reccu(N//3,a+x*N//3,b+y*N//3)
        return
                
  if first_element==-1: ans1+=1
  elif first_element==0: ans2+=1
  elif first_element==1: ans3+=1
    

reccu(N,0,0)
print(ans1)
print(ans2)
print(ans3)