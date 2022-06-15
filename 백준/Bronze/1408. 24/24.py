A = list(map(int,input().split(':')))
B = list(map(int,input().split(':')))

H,M,S = B[0]-A[0],B[1]-A[1],B[2]-A[2]

if S<0 :
    S+=60
    M-=1
if M<0 :
    M+=60
    H-=1
if H<0: H+=24

print("%02d:%02d:%02d" %(H,M,S))