import sys
N = int(sys.stdin.readline())

for _ in range(N):
    temp_list = map(int,sys.stdin.readline().split())
    temp_list = sorted(temp_list, reverse=True)
    print(temp_list[2])