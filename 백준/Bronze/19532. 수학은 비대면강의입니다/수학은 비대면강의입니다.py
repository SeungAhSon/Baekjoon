import sys

a,b,c,d,e,f = map(int, sys.stdin.readline().split())
print((c*e-b*f)//(a*e-b*d), (a*f-d*c)//(a*e-b*d))