import sys
N, K= map(int,sys.stdin.readline().split())
temp_list = list(map(int,sys.stdin.readline().split()))
sum_list = []
for i in range(N-K+1):
    sum_list.append(sum(temp_list[i:i+K]))
print(max(sum_list))