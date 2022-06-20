N = int(input())
A = list(map(int,input().split()))
B,C = map(int, input().split())

ans = N
for i in range(N):
    if (A[i]-B)>0 :
        if ((A[i]-B)%C==0) : ans += (A[i]-B)//C
        else : ans += (A[i]-B)//C+1
print(ans)