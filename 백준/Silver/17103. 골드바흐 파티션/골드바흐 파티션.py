import sys

#에라토스테네스의 체
n=1000001
is_prime = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if is_prime[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        is_prime[j] = False

#수행
T = int(sys.stdin.readline())

for _ in range(T):
    ans = 0
    N = int(sys.stdin.readline())
    for i in primes:
        if i >= N: break
        if is_prime[N-i] and i<=N-i:  ans+=1
    print(ans)