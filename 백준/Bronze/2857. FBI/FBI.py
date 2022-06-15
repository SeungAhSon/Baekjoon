#처음에 한 이름 안에 FBI가 여러번 있을 경우를 고려하지 못해서 23%에서 틀렸습니다가 떴다.
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
