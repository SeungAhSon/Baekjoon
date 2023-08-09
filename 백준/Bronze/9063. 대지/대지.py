import sys

N = int(sys.stdin.readline())

min_x, min_y, max_x, max_y = float("inf"),float("inf"),float('-inf'),float('-inf')

for _ in range(N):
    a,b = map(int, sys.stdin.readline().split())
    min_x = min(min_x, a)
    min_y = min(min_y, b)
    max_x = max(max_x, a)
    max_y = max(max_y, b)

print((max_x-min_x)*(max_y-min_y))