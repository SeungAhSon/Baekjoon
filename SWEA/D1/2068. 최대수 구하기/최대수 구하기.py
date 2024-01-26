T = int(input())
for i in range(1, T + 1):
    ans = list(map(int, input().split()))
    ans.sort()
    print("#%d %d" %(i, ans[9]))
