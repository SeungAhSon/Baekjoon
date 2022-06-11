while(True):
    S = input()
    if S=='0' : break
    
    while(len(S)!=1):
        temp = 1
        print(S, end = " ")
        for i in S:
            temp *= int(i)
        S = str(temp)
    print(S)