def solution(polynomial):
    poly = list(map(str,polynomial.split(" + ")))
    a = []
    b = []
    for i in poly:
        if i[-1]=='x':
            a.append(1 if len(i)==1 else int(i[0:-1]))
        else : b.append(int(i))
        
    a,b=sum(a),sum(b)
    if a==0:
        if b==0: return ''
        else : return str(b)
    elif a==1: 
        if b==0: return 'x'
        else : return 'x + '+str(b)
    else:
        if b==0: return str(a)+'x'
        else: return str(a)+'x + '+str(b)