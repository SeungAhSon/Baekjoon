while True:
    N = int(input())
    if N==0 : break
    
    dic = []
    for _ in range(N):
        dic.append(input())
    dic.sort(key=str.lower)
    print(dic[0])