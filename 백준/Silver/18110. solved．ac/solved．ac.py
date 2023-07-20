import sys

def roundTraditional(val): #사사오입, stackoverflow 참고
    if val-int(val)>=0.5:
        return int(val)+1
    else:
        return int(val)

N = int(sys.stdin.readline())
if N==0: print(0)
else :
    opi = sorted([int(input()) for _ in range(N)])

    trimmed = roundTraditional(N*0.15)
    if trimmed > 0 : opi = opi[trimmed:-trimmed]
    print(roundTraditional(sum(opi)/(N-trimmed*2)))