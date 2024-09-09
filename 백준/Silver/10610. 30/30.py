import sys

N = list(sys.stdin.readline().rstrip())
N.sort()

if N[0]=='0' and sum([int(i) for i in N])%3==0:
  print(''.join(N[::-1]))

else: 
  print(-1)