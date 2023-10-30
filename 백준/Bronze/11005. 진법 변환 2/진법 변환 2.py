import sys

N, B = map(int, sys.stdin.readline().split())
ans = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while N:
    ans+=str(arr[N%B])
    N//=B

print(ans[::-1])