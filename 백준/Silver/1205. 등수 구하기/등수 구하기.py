import sys

N, T, P = map(int, sys.stdin.readline().split())
if N==0 : print(1)
else:
  rank = list(map(int, sys.stdin.readline().split()))
  rank.append(T)
  rank.sort(reverse=True)
  
  #T 태수의 점수가 있는 인덱스를 확인한다.
  temp = rank.index(T)+1
  if temp>P: print(-1)
  else:
    if N==P and T==rank[-1]: print(-1)
    else : print(temp)