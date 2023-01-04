A = list(map(int, input()))

ans = [0] * 9
for i in A:
    if i == 9 : ans[6] += 1
    else : ans[i] += 1
        
ans[6] = int(ans[6]/2)+(ans[6]%2>0)
print(max(ans))