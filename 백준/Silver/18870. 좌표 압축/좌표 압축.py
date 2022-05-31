import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

coordinate = sorted(list(set(arr)))
dic = {coordinate[i] : i for i in range(len(coordinate))}
for i in arr:
    print(dic[i], end = ' ')