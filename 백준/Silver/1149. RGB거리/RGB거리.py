import sys

N = int(sys.stdin.readline())
price = []
for _ in range(N):
    price.append(list(map(int, sys.stdin.readline().split())))
#-----

for i in range(1,N):
    price[i][0]+=min(price[i-1][1],price[i-1][2])
    price[i][1]+=min(price[i-1][0],price[i-1][2])
    price[i][2]+=min(price[i-1][0],price[i-1][1])

print(min(price[-1]))