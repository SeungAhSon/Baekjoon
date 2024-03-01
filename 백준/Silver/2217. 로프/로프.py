import sys

N = int(sys.stdin.readline())

rope = []
for _ in range(N):
  rope.append(int(sys.stdin.readline()))

rope.sort(reverse=True)

ans_list = []
for k in range(N):
  ans_list.append((k+1)*rope[k])

print(max(ans_list))