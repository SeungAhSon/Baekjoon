N = int(input())
trophy = [int(input()) for _ in range(N)]
LC = RC = 0
LM = RM = 0
for n in trophy:
    if n > LM:
        LM = n
        LC += 1
for n in trophy[::-1]:
    if n > RM:
        RM = n
        RC += 1
print(LC)
print(RC)