import sys

while True:
    N = int(sys.stdin.readline())
    if N == 0:  break
    li = list(map(int, input().split()))
    J = 0
    M = 0
    for i in li:
        if i == 1:  J += 1
        else:  M += 1
    print(f"Mary won {M} times and John won {J} times")