import sys

N,M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

total = [0]
for i in range(N):
    total.append(total[i]+num[i])
    
for _ in range(M):
    A,B = map(int, sys.stdin.readline().split())
    print(total[B]-total[A-1])