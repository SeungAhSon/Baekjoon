Cash = int(input())

T = int(input())

cost = 0
for _ in range(T):
    A,B = map(int,input().split())
    cost += A*B

if Cash == cost : print("Yes")
else : print("No")