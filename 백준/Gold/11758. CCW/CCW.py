import sys

dot1 = list(map(int, sys.stdin.readline().split()))
dot2 = list(map(int, sys.stdin.readline().split()))
dot3 = list(map(int, sys.stdin.readline().split()))


def ccw(a,b,c):
  #a, b, c를 순서대로 이은 선분이 어떤 방향을 이루고 있는지
  return (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]-(b[0]*a[1]+c[0]*b[1]+a[0]*c[1]))
    

if ccw(dot1, dot2, dot3) <0: print(-1)
elif ccw(dot1, dot2, dot3) ==0: print(0)
else: print(1)