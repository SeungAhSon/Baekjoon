while(True):
    N = int(input())
    if N==-1 : break
    
    ans = []
    for i in range(1,N//2+1):
        if N%i==0 : ans.append(i)
        
    if(sum(ans)!=N) : print(N,"is NOT perfect.")
    else : print("%d = %s" %(N," + ".join(list(map(str, ans)))))
