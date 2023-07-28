import sys

num_list = [i+1 for i in range(20)]
for _ in range(10):
    a,b = map(int, sys.stdin.readline().split())
    num_list = num_list[:a-1]+ num_list[a-1:b][::-1]+num_list[b:]

print(' '.join(map(str,num_list)))