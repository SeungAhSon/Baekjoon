A,B,C = map(int, input().split())

if(A==B==C) : print("*")
else : 
    if(B==C) : print("A")
    elif(A==C) : print("B")
    elif(A==B) : print("C")