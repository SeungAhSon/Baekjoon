N = int(input())

lotto = input()
count = 0
flag = 0
for i in range(len(lotto)-1):
    if abs(ord(lotto[i+1])-ord(lotto[i]))==1 : count += 1
    else : count = 0
    
    if count==4 :
        flag = 1
        break
    
print("YES" if flag else "NO")
    