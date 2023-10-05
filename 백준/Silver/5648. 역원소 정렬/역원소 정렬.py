import sys

N, *S = sys.stdin.read().split()
S = sorted([int(i[::-1]) for i in S])

for i in S:  print(i)