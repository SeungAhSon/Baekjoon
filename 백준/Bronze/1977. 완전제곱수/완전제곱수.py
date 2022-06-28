M = int(input())
N = int(input())

ans = []
i = 1
while i*i<=N:
    if M<=i*i: ans.append(i*i)
    i+=1
    
if len(ans)==0 : print(-1)
else:
    print(sum(ans))
    print(ans[0])