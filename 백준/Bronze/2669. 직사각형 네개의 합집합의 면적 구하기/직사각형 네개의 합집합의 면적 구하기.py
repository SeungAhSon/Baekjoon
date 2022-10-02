paper = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            paper[i][j] = 1


print(sum(sum(i) for i in paper))