N = int(input())
cloth = list(map(int, input().split()))
if N == 1 and cloth[0]==1: print("Happy")
else :
    cloth.sort()
    if cloth[-1]*2>sum(cloth) : print("Unhappy")
    else : print("Happy")
