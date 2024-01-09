import sys

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

dot1, dot2, dot3, dot4 = [x1, y1], [x2, y2], [x3, y3], [x4, y4]

def ccw(a, b, c):
    return (a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - (b[0] * a[1] + c[0] * b[1] + a[0] * c[1]))

def overlap(a, b, c, d):
    return max(a, b) >= min(c, d) and max(c, d) >= min(a, b)

if ccw(dot1, dot2, dot3) * ccw(dot1, dot2, dot4) <= 0 and ccw(dot3, dot4, dot1) * ccw(dot3, dot4, dot2) <= 0:
    if overlap(x1, x2, x3, x4) and overlap(y1, y2, y3, y4):  print(1)
    else:  print(0)
else:  print(0)
