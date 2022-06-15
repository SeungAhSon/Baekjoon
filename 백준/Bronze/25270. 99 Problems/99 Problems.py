N = int(input())

if N<149 : print("99")
elif N==149 : print("199")
else :
    count = 1
    while(abs(N-(count*100+99))>50):
        count+=1
        
    if(abs(N-(count*100+99))==50) : count +=1
    
    if count>=99 : count = 99
    print(count*100+99)