T = int(input())
for _ in range(T):
    
    A,B = map(int,input().split())
    
    sentence = input()
    
    ans = []
    for i in sentence :
        ans.append(chr((A*(ord(i)-65)+B)%26+65))
    print(*ans, sep = "")