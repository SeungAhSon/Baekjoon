A,B = map(int, input().split())
print(A//B, end = '')

if A%B:
    print('.', end='')
    i = 0
    while A%B and i < 1000: 
        A = A%B*10 
        i += 1
        print(A//B, end = '')