import sys

T = int(sys.stdin.readline())
for _ in range(T):
  x1,y1,r1,x2,y2,r2 = map(int, sys.stdin.readline().split())
  temp = ((x1-x2)**2+(y1-y2)**2)**(1/2)
  
  #내접 또는 외접, 두 점에서 만나는 경우 
  if r1==r2 and x1==x2 and y1==y2 : print(-1)
  elif abs(r1-r2)==temp or r1+r2==temp : print(1) 
  elif abs(r1-r2)<temp and temp<(r1+r2):print(2)
  else:  print(0)