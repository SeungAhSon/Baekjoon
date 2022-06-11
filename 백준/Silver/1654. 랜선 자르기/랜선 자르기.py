K,N = map(int, input().split())
lan = []

for _ in range(K):
    lan.append(int(input()))

low = 1
high = max(lan)
while(low<=high):
    mid = (low+high)//2
    count = 0
    for i in lan : 
        count += i//mid
    if(count>=N): low = mid+1
    else : high = mid-1
print(high)
    