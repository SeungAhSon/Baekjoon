P,K = map(int, input().split())
if P<K: print(P+1000-K)
else: print(P-K+1)
