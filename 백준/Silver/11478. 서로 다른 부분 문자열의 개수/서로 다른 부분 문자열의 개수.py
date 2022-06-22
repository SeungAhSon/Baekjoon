import sys

S = sys.stdin.readline().rstrip('\n')
ans = []

for i in range(len(S)):
    for j in range(i, len(S)):
        temp = S[i:j+1]
        ans.append(temp)
print(len(set(ans)))