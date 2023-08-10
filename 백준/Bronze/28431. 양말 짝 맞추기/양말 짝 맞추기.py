import sys
from collections import defaultdict

socks = defaultdict(int)

for _ in range(5):
    socks[int(sys.stdin.readline())] += 1

for i in socks:
    if socks[i]%2==1 :
        print(i)
        break