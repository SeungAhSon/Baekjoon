import sys
#리스트는 시간초과, 딕셔너리는 해시맵
N = int(sys.stdin.readline())
worker = {}
for _ in range(N):
  a,b = sys.stdin.readline().rstrip().split()
  if a in worker: del worker[a]
  else: worker[a]=1

worker = sorted(worker.keys(), reverse=True)
for i in worker:
  print(i)