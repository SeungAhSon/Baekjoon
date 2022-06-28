N = int(input())
test = list(map(int, input().split()))

count = 0
ans = 0
for i in range(len(test)):
    if test[i]==1:
        count+=1
        ans += count
    else : count = 0
    
print(ans)