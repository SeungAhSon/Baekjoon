import sys

T = int(sys.stdin.readline())

for _ in range(T):
  x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
  n = int(sys.stdin.readline())
  count = 0
  for _ in range(n):
    cx,cy,r = map(int, sys.stdin.readline().split())
    #출발점과 도착점 중 하나가 행성계 안에 위치한다면 count++
    dis1 = (x1 - cx)**2 + (y1 - cy)**2
    dis2 = (x2 - cx)**2 + (y2 - cy)**2
    pow_cr = r**2
        
    if pow_cr > dis1 and pow_cr > dis2: pass
    elif pow_cr > dis1: count += 1
    elif pow_cr > dis2: count += 1
            
  print(count)