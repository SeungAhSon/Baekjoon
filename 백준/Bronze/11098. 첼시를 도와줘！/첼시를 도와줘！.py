N=int(input())

for _ in range(N):
    P=int(input())
    A_List=[]
    B_List=[]
    for _ in range(P):
        A, B=input().split()
        A=int(A)
        A_List.append(A)
        B_List.append(B)

    idx=A_List.index(max(A_List))
    print(B_List[idx])