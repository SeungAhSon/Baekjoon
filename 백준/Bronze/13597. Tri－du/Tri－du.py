import sys
A, B = map(int, sys.stdin.readline().split())
print(A if A == B else max(A, B))