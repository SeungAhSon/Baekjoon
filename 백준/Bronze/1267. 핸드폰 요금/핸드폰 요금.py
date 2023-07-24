import sys

N = int(sys.stdin.readline())

call_list = list(map(int,sys.stdin.readline().split()))

fee1 = sum((i//30+1)*10 for i in call_list)
fee2 = sum((i//60+1)*15 for i in call_list)

if fee1<fee2:
    print("Y", fee1)
elif fee1==fee2:
    print("Y M", fee1)
else:
    print("M", fee2)