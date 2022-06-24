A,B,C = map(int, input().split())

ans = [0]*81
for i in range(1,A+1):
    for j in range(1,B+1):
        for k in range(1,C+1):
            ans[i+j+k]+=1

print(ans.index(max(ans)))