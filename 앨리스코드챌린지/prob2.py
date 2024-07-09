n, m = map(int, input().split())
temp = list(map(int, input().split()))

for _ in range(m):
    i,j,k = map(int, input().split())
    temp2 = sorted(temp[i-1:j])
    print(temp2[k-1])
