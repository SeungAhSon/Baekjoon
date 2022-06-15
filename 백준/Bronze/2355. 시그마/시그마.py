import sys
A,B = map(int,sys.stdin.readline().split())

max_value = max(A, B)
min_value = min(A, B)

sum = int((A+B)*(max_value-min_value+1)/2)
print(sum)