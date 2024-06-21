import sys

def quad_tree(x,y,M):
    initial = img[x][y]
    for i in range(x, x + M):
        for j in range(y, y + M):
            if img[i][j] != initial:
                half = M // 2
                top_left = quad_tree(x, y, half)
                top_right = quad_tree(x, y + half, half)
                bottom_left = quad_tree(x +half, y, half)
                bottom_right = quad_tree(x + half, y + half, half)
                return f"({top_left}{top_right}{bottom_left}{bottom_right})"
    return initial

#=========
N = int(sys.stdin.readline())
img = []

for _ in range(N):  img.append(list(sys.stdin.readline().rstrip()))

print(quad_tree(0,0,N))