#첫 시도는 시간초과

#prime_list
prime_list = [2]
for i in range(3, int(10000000 ** (0.5)), 2):
    for p in prime_list:
      if not i%p: break
    else:  prime_list.append(i)
        
T = int(input())
ans_list = []
for i in range(T):
  N = int(input())
  factors = {}
  ans = 1
  if N**0.5 != int(N**0.5):
    for p in prime_list:
      cnt = 0
      while N%p==0:
        cnt+=1
        N//=p
      if cnt%2: ans*=p
      if N==1 or p>N:  break
    if N > 1:  ans*=N
  
  for j in list(factors.keys()):
    if factors[j]%2!=0: ans*=j
  ans_list.append("#%d %s"%(i+1,ans))

for i in ans_list:
  print(i)

