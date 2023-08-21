import sys
from collections import defaultdict
N,M = map(int, sys.stdin.readline().split())

pass_dict = defaultdict(str)
for _ in range(N):
    a,b= sys.stdin.readline().rstrip().split()
    pass_dict[a] = b
  
for _ in range(M):
    a = sys.stdin.readline().rstrip()
    print(pass_dict[a])