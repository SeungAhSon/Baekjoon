#정인이는 적어도 1초를 기다리며, 많아야 24시간을 기다린다.(84%)
A = list(map(int,input().split(':')))
B = list(map(int,input().split(':')))

if (A==B) : print("24:00:00")
else :
    H,M,S = B[0]-A[0],B[1]-A[1],B[2]-A[2]
    
    if(H==0 and M==0 and S==0) : print("00:00:01")
    else : 
        if S<0 :
            S+=60
            M-=1
        if M<0 :
            M+=60
            H-=1
        if H<0: H+=24
        
        if (H>=24) : print("24:00:00")
        else : print("%02d:%02d:%02d" %(H,M,S))