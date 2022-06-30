import sys
from collections import deque

N = int(sys.stdin.readline())
Q = deque([])
for _ in range(N):
    s = sys.stdin.readline().split()
    
    if s[0] == 'push': Q.append(s[1])
    elif s[0] == 'pop':
        if not Q: print(-1)
        else: print(Q.popleft())
    elif s[0] == 'size': print(len(Q))
    elif s[0] == 'empty':
        if not Q: print(1)
        else: print(0)
    elif s[0] == 'front':
        if not Q: print(-1)
        else: print(Q[0])
    elif s[0] == 'back':
        if not Q: print(-1)
        else: print(Q[-1])