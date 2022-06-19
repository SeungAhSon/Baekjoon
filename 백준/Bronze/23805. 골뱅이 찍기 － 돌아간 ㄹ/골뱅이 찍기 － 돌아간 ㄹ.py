N = int(input())

for i in range(5*N):
    if i<N : print("@"*3*N+" "*N+"@"*N)
    elif 4*N<=i : print("@"*N+" "*N+"@"*3*N)
    else : print("@"*N +" "*N +"@"*N+" "*N +"@"*N)