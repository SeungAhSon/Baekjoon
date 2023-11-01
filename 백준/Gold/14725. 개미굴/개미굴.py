import sys

N = int(sys.stdin.readline())

ant = []
for _ in range(N):
  ant.append(sys.stdin.readline().split()[1:])
ant.sort()

dash = '--'
ans = []
for i in range(N):
  if i==0:
    for j in range(len(ant[i])):
      ans.append(dash*j+ant[i][j])
  else:
    idx = 0
    for j in range(len(ant[i])):
      if ant[i-1][j]!=ant[i][j] or len(ant[i-1])<=j: break
      else: idx = j + 1
    for j in range(idx,len(ant[i])):  ans.append(dash*j+ant[i][j])
  
print('\n'.join(ans))


"""
반례 입력 :
2
2 A ABC
2 A A

출력 : 
A
--A
--ABC
"""