N = int(input())

for i in range(5*N):
    if i<N : print("@"*N+" "*3*N+"@"*N)
    elif N<=i<2*N : print("@"*N+" "*2*N+"@"*N)
    elif 2*N<=i<3*N : print("@@@"*N)
    elif 3*N<=i<4*N :print("@"*N+" "*2*N+"@"*N)
    elif 4*N<=i : print("@"*N+" "*3*N+"@"*N)