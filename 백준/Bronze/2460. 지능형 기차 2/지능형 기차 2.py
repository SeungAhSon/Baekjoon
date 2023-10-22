import sys

temp = max_temp = 0
for _ in range(10):
  a,b = map(int, sys.stdin.readline().split())
  temp += b-a
  max_temp = max(max_temp, temp)

print(max_temp)