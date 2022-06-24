N,M,K = map(int, input().split())
while K-3 <= 0: K += N

if (((K-3)%N)+M)%N==0 : print(N)
else : print((((K-3)%N)+M)%N)