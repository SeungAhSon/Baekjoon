import sys
from datetime import date

while True :
    a,b,c = map(int,sys.stdin.readline().split())
    if a==b==c==0 : break
    temp = date(c,b,a)
    temp2 = date(c,1,1)
    print((temp-temp2).days+1)