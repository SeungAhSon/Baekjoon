import sys

N, r, c = map(int,sys.stdin.readline().split())

ans = 0
while N>1:
  temp = 2**(N-1)
  
  if r<temp and c<temp: pass
  elif r<temp and c>=temp:
    ans+=temp**2
    c-=temp
  elif r>=temp and c<temp:
    ans+=2*(temp**2)
    r-=temp
  elif r>=temp and c>=temp:
    ans+=3*(temp**2)
    r-=temp
    c-=temp
  N-=1
 
if r==0 and c==0 : print(ans)
elif r==0 and c==1: print(ans+1)
elif r==1 and c==0: print(ans+2)
elif r==1 and c==1 : print(ans+3)