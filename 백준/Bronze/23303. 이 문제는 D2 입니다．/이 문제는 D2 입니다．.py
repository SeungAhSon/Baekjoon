string = list(input())

if(len(string)<2) : print("unrated")

flag = 0
for i in range(len(string)-1):
    if((string[i]+string[i+1])=="D2" or (string[i]+string[i+1])=="d2"):
        flag = 1
if flag == 0 : print("unrated")
else : print("D2")