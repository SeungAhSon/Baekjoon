A,B = map(int, input().split())

a = []
for i in range(B+1) :
    for j in range(i):
        if len(a) == B : break
        a.append(i)
print(sum(a[A-1:B]))