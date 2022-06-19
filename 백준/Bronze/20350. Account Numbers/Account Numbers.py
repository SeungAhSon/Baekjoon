account = input()

account = account[4:]+account[0:4]

ans = []
for i in account:
    if i.isalpha():
        ans.append(str(ord(i)-55))
    else : ans.append(str(i))
    
ans = int("".join(ans))

if ans%97==1 : print("correct")
else : print("incorrect")