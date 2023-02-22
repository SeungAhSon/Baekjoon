while(True):
    sentence = input()
    if sentence==".": break

    stack = []
    for i in sentence:
        if i=='[' or i=='(': stack.append(i)
        elif i==']':
            if len(stack)>=1 and stack[-1]=='[': stack.pop()
            else : stack.append(']')
        elif i==')':
            if len(stack)>=1 and stack[-1]=='(': stack.pop()
            else : stack.append(')')
    
    if len(stack)==0: print("yes")
    else: print("no")