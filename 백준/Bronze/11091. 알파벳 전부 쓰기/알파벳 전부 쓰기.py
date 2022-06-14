N = int(input())

for i in range(N):
    alpha = [0]*26
    string = input()
    for j in string:
        if(ord(j.lower())-97>=0):
            alpha[ord(j.lower())-97] += 1
            
    ans = ""
    for j in range(0,26):
        if(alpha[j]==0) : ans += chr(j+97)
    
    if len(ans)==0 : print("pangram")
    else : print("missing",ans)