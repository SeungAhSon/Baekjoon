import sys

N = int(sys.stdin.readline())
distance = list(map(int,sys.stdin.readline().split())) #3, 도로의 길이
gas  = list(map(int,sys.stdin.readline().split())) #4, 주유소 리터당 가격


# 기름 가격이 싼 도시가 나올때까지 거리 더하기
# 싼 도시가 나오면 기름갑 & 거리
i = 0
ans = 0
temp_dist = 1

while (i+temp_dist) < (N):
    if gas[i] > gas[i+temp_dist]:
        ans += gas[i]*sum(distance[i:(i+temp_dist)])
        i += temp_dist
        temp_dist = 1
    
    else:  temp_dist += 1
        
ans += gas[i]*sum(distance[i:])
       
print(ans)