#python3로는 시간초과가 나고, pypy로 하면 통과되었다.

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
