import sys
#4635랑 같은 문제
while True:
    N = int(sys.stdin.readline())
    if N == -1: break
    last_time = 0
    distance = 0
    for _ in range(N):
        s, t = map(int, sys.stdin.readline().split())
        distance += s*(t-last_time)
        last_time = t
    print(f"{distance} miles")
