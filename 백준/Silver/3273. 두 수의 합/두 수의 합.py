import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

pairs = 0
num_count = {}

for i in arr:
  if x-i in num_count: pairs+=num_count[x-i]
  if i in num_count: num_count[i] += 1
  else: num_count[i] = 1

print(pairs)
