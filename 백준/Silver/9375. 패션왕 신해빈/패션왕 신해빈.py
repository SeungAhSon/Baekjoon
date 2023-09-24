import sys

T = int(sys.stdin.readline())
for _ in range(T):
  clo_dict = dict()
  
  N = int(sys.stdin.readline())
  for _ in range(N):
    a,b= sys.stdin.readline().rstrip().split()
    if b not in clo_dict: clo_dict[b] = 0
    clo_dict[b]+=1

  count = 1
  for i in clo_dict.keys():
    count *= clo_dict[i]+1
  print(count-1)