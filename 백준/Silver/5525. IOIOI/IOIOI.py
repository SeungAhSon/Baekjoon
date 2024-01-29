import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()


"""
#subtask1만 통과하게 된다.
P = 'IO'*N + 'I'
ans = 0
for i in range(M -2*N-1):
  if S[i] == 'I' and S[i:i+len(P)] == P:  ans += 1
print(ans)
"""
#subtask2도 통과
ans, count, i = 0,0,0
while i<M-1:
  if S[i:i+3]=="IOI":
    i+=2
    count+=1
    if count==N:
      ans+=1
      count-=1
  else:
    i+=1
    count=0

print(ans)