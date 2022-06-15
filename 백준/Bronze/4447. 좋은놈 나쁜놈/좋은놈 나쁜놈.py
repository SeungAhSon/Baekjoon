import sys

N = int(sys.stdin.readline())
for _ in range(N):
    name = sys.stdin.readline().rstrip('\n')
    
    
    countg = name.count('g') + name.count("G")
    countb = name.count('b') + name.count("B")
    
    if countb>countg : print(name,"is A BADDY")
    elif countb==countg : print(name,"is NEUTRAL")
    else : print(name,"is GOOD")
