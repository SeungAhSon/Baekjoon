import sys

Ax1, Ay1, Ax2, Ay2 = map(int, sys.stdin.readline().split())
Bx1, By1, Bx2, By2 = map(int, sys.stdin.readline().split())

if min(Ax1, Bx1)==Bx1:
  #만약에 B가 상대적으로 왼쪽에 있는 경우, A랑 바꿔주기
  Ax1, Bx1 = Bx1, Ax1
  Ay1, By1 = By1, Ay1
  Ax2, Bx2 = Bx2, Bx2
  Ay2, By2 = By2, Ay2

ans = ""
if Ax2==Bx1:
  if Ay2==By1 or Ay1==By2:  ans="POINT"
  elif Ay1<=By1<=Ay2 or Ay1<=By2<=Ay2 or By1<=Ay1<=By2:  ans="LINE"
elif Ax2 > Bx1:
  if By2<Ay1 or Ay2<By1:  ans="NULL"
  elif By2==Ay1 or Ay2==By1:  ans="LINE"
  else:  ans="FACE"
  
if ans=="": print("NULL")
else: print(ans)
