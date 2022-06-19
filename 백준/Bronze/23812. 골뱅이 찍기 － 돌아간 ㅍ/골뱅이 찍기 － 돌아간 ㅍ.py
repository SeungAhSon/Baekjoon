N = int(input())

for i in range(5*N):
    if N<=i<2*N or 3*N<=i<4*N : print("@@@@@"*N)
    else : print("@"*N + " "*(3*N) + "@"*N)