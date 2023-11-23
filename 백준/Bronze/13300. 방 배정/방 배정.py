import sys
import math

N, K = map(int, sys.stdin.readline().split())
temp = [[0] * 7 for _ in range(3)]

for _ in range(N) :
  S, Y = map(int, sys.stdin.readline().split())
  temp[S][Y] += 1

num = 0
for i in temp :
  for j in i :  num += math.ceil(j / K)

print(num)