import sys
import math

D,H,W = map(int, sys.stdin.readline().split())
a = math.sqrt(D**2/(H**2+W**2))
print(math.floor(H*a), math.floor(W*a))