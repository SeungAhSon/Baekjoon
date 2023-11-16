import sys

N = int(sys.stdin.readline())
ans = 0
for _ in range(N):
    x = sys.stdin.readline().rstrip()
    if x=="ENTER":  new_chat = {}
    elif x not in new_chat:
      new_chat[x]=1
      ans += 1
print(ans)