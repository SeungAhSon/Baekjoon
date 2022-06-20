R,C,N = map(int, input().split())

print((R//N+1 if R%N else R//N)*(C//N+1 if C%N else C//N))