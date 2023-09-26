import sys
N = int(sys.stdin.readline())

for i in range(N) :
  data = sys.stdin.readline().rstrip()
  print('%d. %s' % (i+1, data))