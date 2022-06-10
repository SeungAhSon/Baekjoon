def check():
    for i in range(len(phone)-1):
        if phone[i]==phone[i+1][:len(phone[i])]:
            print("NO")
            return
    print("YES")

T = int(input())

for _ in range(T):
    N = int(input())
    phone = []
    for i in range(N):
        phone.append(input().strip())
    phone.sort()
    check()