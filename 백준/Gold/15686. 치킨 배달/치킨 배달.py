def calculate_dist(house, chicken):
    sum_dist = 0
    for i in house:
        min_dist = float('inf')
        for j in chicken:
            temp = abs(i[0]-j[0])+abs(i[1]-j[1])
            min_dist = min(min_dist, temp)
        sum_dist+= min_dist
    return sum_dist

def Combinations(arr, n):
    ans = []

    if n==0: return [ans]

    for i in range(len(arr)):
        temp = arr[i]
        rest = arr[i+1:]
        for j in Combinations(rest, n-1):
            ans.append([temp]+j)
    return ans


N,M = map(int, input().split())
field = list(list(map(int, input().split())) for _ in range(N))

list_house = []
list_chicken = []
for i in range(N):
    for j in range(N):
        if field[i][j]==1: list_house.append([i,j])
        elif field[i][j]==2: list_chicken.append([i,j])

combins = Combinations(list_chicken, M)
ans = float('inf')
for i in combins:
    ans = min(ans, calculate_dist(list_house, i))
print(ans)