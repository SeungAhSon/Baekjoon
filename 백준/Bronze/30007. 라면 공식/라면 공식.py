N = int(input())
for i in range(N) : 
    A, B, X = map(int ,input().split())
    print(A * (X - 1) + B)