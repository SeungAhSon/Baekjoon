import sys
#이분탐색

T=int(sys.stdin.readline())

for _ in range(T):
    n,s=map(int, sys.stdin.readline().split())
    L=sorted(list(map(int, sys.stdin.readline().split())))
    
    start=1
    end=max(L)
    
    while start<=end:
        mid=(start+end)//2
        a=L[0]
        count=1
        for i in range(1,n):
            b=L[i]
            if abs(b-a)>=mid:
                count+=1
                a=L[i]
        if count>=s:  start=mid+1
        else:  end=mid-1
    print(end)