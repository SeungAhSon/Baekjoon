import sys
import collections

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

temp = str(A*B*C)

elements_count = [0]*10
for i in temp:
  elements_count[int(i)]+=1

for i in elements_count:
  print(i)