#왼쪽 오른쪽 여백도 고려해야한다
import sys
while True:
    string = sys.stdin.readline().rstrip('\n')
    if not string : break
    a,b,c,d=0,0,0,0
    for temp in string:
        if temp.islower(): a+=1
        elif temp.isupper(): b+=1
        elif temp.isdigit(): c+=1
        elif temp.isspace(): d+=1
        
    print(a,b,c,d)