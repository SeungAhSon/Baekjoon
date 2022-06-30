import sys
N,M = map(int,sys.stdin.readline().split())

for _ in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    for i in range(0,len(row)-2,3):
        temp = 2126*row[i]+7152*row[i+1]+722*row[i+2]
        if(0<=temp<510000): print('#',end='')
        elif(510000<=temp<1020000): print('o',end='')
        elif(1020000<=temp<1530000): print('+',end='')
        elif(1530000<=temp<2040000): print('-',end='')
        elif(2040000<=temp): print('.',end='')
    print()