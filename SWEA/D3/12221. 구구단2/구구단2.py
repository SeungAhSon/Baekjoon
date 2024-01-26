T = int(input())
for test_case in range(1, T + 1):
    a,b = map(int, input().split())
    if a<10 and b<10:  print("#%d %s"%(test_case, a*b))
    else: print("#%d -1"%(test_case))
