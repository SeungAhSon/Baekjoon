import sys
left = ['q','w','e','r','t','a','s','d','f','g','z','x','c','v','b']
right = ['y','u','i','o','p','h','j','k','l','n','m']

flag=1
prev=-1
curr=0


word = sys.stdin.readline()[:-1]
for i in word :
    if i in left : curr = 0
    else : curr = 1
    
    if prev==curr :
        flag = 0
        break
    
    prev=curr
        
print('yes' if flag else 'no')