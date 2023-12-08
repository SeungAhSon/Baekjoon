import sys
import heapq

N = int(sys.stdin.readline())
temp = sys.stdin.readline().rstrip()

count = 0
for i in temp:
  if i in ['a','i','u','e','o']: count+=1

print(count)