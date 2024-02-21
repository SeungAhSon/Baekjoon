import sys

hanger_type = [0,0,0]
N = int(sys.stdin.readline())
A_list = list(map(int,sys.stdin.readline().split()))
U, D = map(int, sys.stdin.readline().split())

for A in A_list:  hanger_type[A-1]+=1
  
a = U-hanger_type[0]
b = D-hanger_type[1]

if a>=0 and b>=0 and a+b==hanger_type[2]:
  print("YES")

  for A in A_list:
    if A==1: print("U", end="")
    elif A==2: print("D", end="")
    else:
      if a>0:
        print("U", end="")
        a-=1  
      else: print("D", end="")
  
else:  print("NO")