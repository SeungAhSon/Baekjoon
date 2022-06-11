T = int(input())
for _ in range(T):
    N = int(input())
    li = sorted(map(int, input().split()))
    print(li[0], li[-1])