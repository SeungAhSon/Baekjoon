i = 1
while 1:
    N = int(input())
    if N == 0: break
    N1 = 3*N
    N2 = (N1+1)//2 if N1%2 else N1//2
    N3 = 3*N2
    N4 = N3//9
    if N == 2*N4: print(f"{i}. even {N4}")
    else: print(f"{i}. odd {N4}")
    i += 1