N = int(input())

for i in range(5*N):
    if i<N or 2*N<=i<3*N : print("@@@@@"*N)
    else : print("@"*N)