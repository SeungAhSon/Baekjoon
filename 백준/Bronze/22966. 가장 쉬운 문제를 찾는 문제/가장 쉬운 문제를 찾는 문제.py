N = int(input())

ans = ""
num = 5

for _ in range(N):
    A, B = map(str, input().split())
    if(int(B)<num):
        num = int(B)
        ans = A

print(ans)