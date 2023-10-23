import sys

temp_list = []

for _ in range(10):  temp_list.append(int(sys.stdin.readline()))

print(int(sum(temp_list)/10))

temp_set = list(set(temp_list))
temp_count = [0]*len(temp_set)

for i in temp_list:
  temp_count[temp_set.index(i)]+=1

print(temp_set[temp_count.index(max(temp_count))])