ans = []
for i in range(5):
    name = input()
    if len(name)<3 : continue
    
    for j in range(len(name)-2):
        if(name[j:j+3]=="FBI") :
            ans.append(i+1)
            break
            

if(len(ans)==0) : print("HE GOT AWAY!")
else : print(*ans, sep = " ")