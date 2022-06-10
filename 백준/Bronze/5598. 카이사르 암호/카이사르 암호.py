Caeser = ['X', 'Y', 'Z', 'A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W']

N = list(input())

ans = []
for i in N:
    ans.append(Caeser[ord(i)-65])
print("".join(ans))