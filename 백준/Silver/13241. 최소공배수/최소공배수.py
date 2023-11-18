import sys

A, B = map(int, sys.stdin.readline().split())
temp = A*B

while B:
  if A>B: A,B = B,A
  B %= A

print(temp//A)