K = list(map(int,input()))

if(len(K)==1) : print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else : 
    flag = 0
    count = K[1]-K[0]
    for i in range(len(K)-1):
        if(count!=(K[i+1]-K[i])) : flag = 1
        
    if flag == 1 : print("흥칫뿡!! <(￣ ﹌ ￣)>")
    else : print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")