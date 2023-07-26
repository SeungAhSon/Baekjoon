import sys

def gcd(a, b):
    while b > 0: a, b = b, a % b
    return a

N = int(sys.stdin.readline())
for _ in range(N):
    a,b = map(int,sys.stdin.readline().split())
    print((a*b)//gcd(a, b))