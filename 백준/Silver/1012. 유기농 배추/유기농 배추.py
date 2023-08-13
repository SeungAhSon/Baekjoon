import sys
sys.setrecursionlimit(10000)

#백준 채점 시스템에서 최대 재귀 깊이는 1000
#최대 재귀 깊이를 늘려줘야 함.
#안 늘리면 12%에서 런타임 에러.


def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < M) and (0 <= ny < N):
            if field[ny][nx] == 1:
                field[ny][nx] = 0
                dfs(nx, ny)

T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    field = [[0 for _ in range(M)] for _ in range(N)]	
    count = 0
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())	
        field[y][x] = 1	
    for x in range(M):
        for y in range(N):
            if field[y][x] == 1:
                dfs(x, y)
                count += 1
    print(count)