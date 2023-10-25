import sys

while True:
  N = int(sys.stdin.readline())
  if N==0:  break
  print(N*(N+1)//2)