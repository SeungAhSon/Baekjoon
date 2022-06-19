N = int(input())

for i in range(5*N):
    if i<N or 4*N<=i : print("@@@@@"*N)
    else : print("@"*N)