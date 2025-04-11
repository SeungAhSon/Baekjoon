N, K = map(int, input().split())
A = list(map(int, input().split()))
R = [0]*N

answer = 0
while True:
    #move_belt
    A = [A[-1]] + A[:-1]
    R = [R[-1]] + R[:-1]
    R[-1] = 0

    #move_robot
    for i in range(N-2,-1,-1):
        if R[i]==1 and R[i+1]==0 and A[i+1]>=1:
            R[i+1] = 1
            R[i] = 0
            A[i+1] -= 1
    R[-1] = 0


    #add_robot
    if R[0]==0 and A[0]>0:
        A[0] -= 1
        R[0] = 1

    answer += 1
    if sum(i==0 for i in A)>=K: break


print(answer)