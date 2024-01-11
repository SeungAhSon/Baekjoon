T = int(input())
for i in range(T):
  A, B = map(int, input().split())
  print("#%d %s"%(i+1,(A+B)%24))