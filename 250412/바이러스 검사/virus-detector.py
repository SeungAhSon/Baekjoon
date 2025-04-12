N = int(input())
Customer = list(map(int, input().split()))
TeamLead, TeamWorker = map(int, input().split())

#가게 당 팀장은 무조건 존재
ans=N
for i in range(N):
    Customer[i] -= TeamLead
    if Customer[i]>0:
        ans+=(Customer[i]//TeamWorker + (1 if Customer[i]%TeamWorker!=0 else 0))
print(ans)