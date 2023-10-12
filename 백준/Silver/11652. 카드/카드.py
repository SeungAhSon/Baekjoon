import sys


N = int(sys.stdin.readline())
num_dict = dict()

for _ in range(N):
  num = int(sys.stdin.readline())
  if num in num_dict:  num_dict[num]+=1
  else: num_dict[num] = 1

sorted_dict = sorted(num_dict.items(), key=lambda item: (-item[1], item[0]))
print(sorted_dict[0][0])
