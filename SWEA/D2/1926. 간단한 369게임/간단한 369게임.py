N = int(input())

for i in range(1, N+1):
    i = str(i)
    flag = i.count('3') + i.count('6') + i.count('9')
    if flag == 0:  print(i, end=' ')
    else:  print("-"*flag, end=' ')