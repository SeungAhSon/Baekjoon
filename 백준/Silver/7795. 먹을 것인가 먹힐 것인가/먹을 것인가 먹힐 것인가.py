import sys
def binary_search(data,target):
  start = 0
  end = len(data) - 1
  res = -1
  while start <= end:
    mid = (start + end) // 2
    if data[mid] < target:
      res = mid
      start = mid + 1
    else:  end = mid -1
  return res
  
T = int(sys.stdin.readline())
for _ in range(T):
  cnt = 0
  N, M = map(int, sys.stdin.readline().split())
  A = sorted(list(map(int, sys.stdin.readline().split())))
  B = sorted(list(map(int, sys.stdin.readline().split())))
  for i in A :  cnt+=binary_search(B,i)+1
  print(cnt)