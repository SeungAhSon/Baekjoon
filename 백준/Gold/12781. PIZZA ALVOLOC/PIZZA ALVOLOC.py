import sys

#네 조각으로 나눠지는지 알아야하므로 ccw를 이용한다.
#17386번과 유사한 문제
x1, y1, x2, y2, x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
dot1, dot2, dot3, dot4 = [x1, y1], [x2, y2], [x3, y3], [x4, y4]

def ccw(a, b, c):
    return (a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - (b[0] * a[1] + c[0] * b[1] + a[0] * c[1]))

if ccw(dot1, dot2, dot3) * ccw(dot1, dot2, dot4) < 0 and ccw(dot3, dot4, dot1) * ccw(dot3, dot4, dot2) < 0:
    print(1)
else:  print(0)
