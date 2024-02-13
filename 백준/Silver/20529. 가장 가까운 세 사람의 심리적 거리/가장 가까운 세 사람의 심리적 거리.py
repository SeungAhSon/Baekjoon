import sys
#단순 브루트포스는 시간초과과 난다. 비둘기집원리를 사용

T = int(sys.stdin.readline())
for _ in range(T):
  N = int(sys.stdin.readline())
  students = list(sys.stdin.readline().rstrip().split())
  if N>32: print(0)
  else: 
    ans = 9999
    for i in range(N):
      for j in range(N):
        for k in range(N):
          if i==j or j==k or k==i: break
          count = 0
          for m in range(4):
            if students[i][m]!= students[j][m]: count+=1
            if students[j][m]!= students[k][m]: count+=1
            if students[k][m]!= students[i][m]: count+=1   
          ans = min(ans, count)
    print(ans)