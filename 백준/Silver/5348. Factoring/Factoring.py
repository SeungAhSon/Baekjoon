import sys

N = int(sys.stdin.readline())

for _ in range(N):
    orig_n = int(sys.stdin.readline())
    n = orig_n
    ans = []
    i = 2
    while i <= n:
        if n % i == 0:
            ans.append(i)
            n = n // i
        else:
            i += 1
    if len(ans) <= 1: print("%d: prime"%(orig_n))
    else : print("%d: %s"%(orig_n,' '.join(map(str,ans))))