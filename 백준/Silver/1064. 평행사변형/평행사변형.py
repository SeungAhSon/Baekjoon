import sys

def distance(x1,y1,x2,y2):
    return(((x1-x2)**2+(y1-y2)**2)**0.5)

xA,yA,xB,yB,xC,yC = map(float,sys.stdin.readline().split())

#만약 기울기가 같다면 만들수가 없다.
if ((xA-xB)*(yA-yC)==(yA-yB)*(xA-xC)):
    print(-1.0)
    exit(0)


dis1 = distance(xA,yA,xB,yB)
dis2 = distance(xA,yA,xC,yC)
dis3 = distance(xB,yB,xC,yC)

candidate = [dis1+dis2, dis1+dis3, dis2+dis3]
print(2*(max(candidate)-min(candidate)))