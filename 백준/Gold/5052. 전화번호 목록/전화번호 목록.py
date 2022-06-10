import sys
T = int(input())

for _ in range(T):
    N = int(input())
    phone = []
    for _ in range(N):
        phone.append(sys.stdin.readline().strip())
    phone.sort()
    
    flag = 1
    for i in range(len(phone)-1):
        if phone[i]==phone[i+1][:len(phone[i])]:
            flag = 0
        
    if flag == 1: print("YES")
    else : print("NO")