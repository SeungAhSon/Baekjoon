N = int(input())
q1=q2=q3=q4=axis=0
for _ in range(N):
    x,y = map(int,input().split())
    if x==0 or y==0 : axis+=1
    elif x>0:
        if y>0:q1+=1
        else:q4+=1
    else:
        if y>0:q2+=1
        else:q3+=1     
print("Q1: %d\nQ2: %d\nQ3: %d\nQ4: %d\nAXIS: %d" %(q1,q2,q3,q4,axis))