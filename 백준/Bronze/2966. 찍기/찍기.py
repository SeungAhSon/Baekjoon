import sys

N = int(sys.stdin.readline())
ans = sys.stdin.readline().rstrip()

A = 'ABC'*(N//3)+'ABC'[:N%3]
B = 'BABC'*(N//4) + 'BABC'[:N%4]
G = 'CCAABB'*(N//6) + 'CCAABB'[:N%6]

a,b,c = 0,0,0
for i in range(N):
  if ans[i]==A[i]:a+=1
  if ans[i]==B[i]:b+=1
  if ans[i]==G[i]:c+=1

print(max(a,b,c))
if max(a,b,c)==a: print('Adrian')
if max(a,b,c)==b: print('Bruno')
if max(a,b,c)==c: print('Goran')