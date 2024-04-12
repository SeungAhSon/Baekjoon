str = input()
ans = ''
for i in str:
    if i.isupper(): ans+=i.lower()
    else: ans+=i.upper()
print(ans)