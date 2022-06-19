N = int(input())

for i in range(5*N):
    if 2*N<=i<3*N or 4*N<=i : print("@@@@@"*N)
    else : print("@"*N + " "*(3*N) + "@"*N)