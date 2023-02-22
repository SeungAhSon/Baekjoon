N=int(input())
ans = ["No","Yes"]

for _ in range(N):
    x,y =map(int,input().strip().split())
    flag1, flag2 = 0,0
    
    #hour and min
    if (x>=0 and x<=23) and (y>=0 and y<=59):
        flag1=1
    
    #month and day
    if (x in [1,3,5,7,8,10,12]) and (y>=1 and y<=31): flag2=1
    elif (x in [4,6,9,11]) and (y>=1 and y<=30): flag2=1
    elif x==2 and (y>=1 and y<=29): flag2=1
    
    #ans
    print(ans[flag1], ans[flag2])
