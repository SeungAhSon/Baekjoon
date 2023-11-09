import sys

N,M = map(int, sys.stdin.readline().split())
word_dict = {} #{'apple': [count, length, 'apple']}

for _ in range(N):
	name = sys.stdin.readline().strip()
	if len(name)>=M:
	  if name in word_dict.keys(): word_dict[name][0] += 1
	  else:	word_dict[name] = [1, len(name), name]
ans = sorted(word_dict.items(), key= lambda x: (-x[1][0], -x[1][1], x[1][2]))

for i in ans:  print(i[0])