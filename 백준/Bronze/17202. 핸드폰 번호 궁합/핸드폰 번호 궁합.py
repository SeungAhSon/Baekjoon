A = list(map(int, input()))
B = list(map(int, input()))

ans = []
for i in range(8):
    ans.append(A[i])
    ans.append(B[i])

while len(ans)>2:
    temp = []
    for i in range(len(ans)-1):
        temp.append((ans[i]+ans[i+1])%10)
    ans = temp
print(ans[0],ans[1],sep="")