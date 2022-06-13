import math
while(True):
    A,B,C = map(float,input().split())
    if(A+B+C==0) : break
    print("Horizontal DPI: %.2f"%(B*(math.sqrt(337)/16/A)))
    print("Vertical DPI: %.2f"%(C*math.sqrt(337)/9/A))