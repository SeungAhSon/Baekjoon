import sys

num = sorted(list(map(int, sys.stdin.readline().split())))

if num[0]==num[1]==num[2]: print(2)
elif num[0]**2 + num[1]**2 == num[2]**2 : print(1)
else: print(0)