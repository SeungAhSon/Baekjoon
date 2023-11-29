import sys

bowl = []
for _ in range(3):
  bowl.append(int(sys.stdin.readline()))
bowl.sort()

print(bowl[1])