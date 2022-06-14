num = list(map(int, input().split()))
N = int(input())

num.append(N)
num.sort(reverse=True)

for i in range(len(num)):
    if num[i]==N:
        if i<5 : print("A+")
        elif i<15 : print("A0")
        elif i<30 : print("B+")
        elif i<35 : print("B0")
        elif i<45 : print("C+")
        elif i<48 : print("C0")
        elif i<50 : print("F")
        break