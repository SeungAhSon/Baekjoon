import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == -1: break
    last_time = 0
    distance = 0
    for _ in range(N):
        s, t = map(int, input().split())
        distance += s*(t-last_time)
        last_time = t
    print(f"{distance} miles")