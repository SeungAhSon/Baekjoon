import sys

while True:
    x,y = map(float, sys.stdin.readline().split())
    if x == 0 or y == 0 : 
        print("AXIS")
        if x==y : break
    elif x>0 :
        if y>0 : print("Q1")
        else : print("Q4")
    else :
        if y>0 : print("Q2")
        else : print("Q3")
        
    