N = int(input())
cloth = list(map(int, input().split()))
if N == 1 and cloth[0]==1: print("Happy")
else :
    if max(cloth)*2>sum(cloth) : print("Unhappy")
    else : print("Happy")
