import sys
N, M, Q = map(int, sys.stdin.readline().split())
operations = [list(map(int, sys.stdin.readline().split())) for _ in range(Q)]

matrix = [[0] * M for _ in range(N)]
row_updates = [0] * N
col_updates = [0] * M

for op in operations:
    if op[0] == 1:
        r, v = op[1], op[2]
        row_updates[r - 1] += v
    elif op[0] == 2:
        c, v = op[1], op[2]
        col_updates[c - 1] += v

for i in range(N):
    for j in range(M):
        matrix[i][j] = row_updates[i] + col_updates[j]

for row in matrix:
    print(*row)