import sys

T = int(sys.stdin.readline())

for _ in range(T):
    C = int(sys.stdin.readline())
    q, C = C//25, C%25
    d, C = C//10, C%10
    n, C = C//5, C%5
    p = C
    print(q,d,n,p)