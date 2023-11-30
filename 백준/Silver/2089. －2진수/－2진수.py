import sys
N = int(sys.stdin.readline())

ans =''
if N == 0:  print(0)
else: 
  while N:
      if N % (-2): 
          ans='1'+ans
          N = N//-2 + 1
      else:
          ans='0'+ans
          N = N//-2
  print(ans)