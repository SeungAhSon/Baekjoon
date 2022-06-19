N = int(input())
ans = 0
for _ in range(N):
    A,B = map(float, input().split())
    B = float(B)/(float(A)/100)**2
    if A<140.1 : ans = 6
    elif 140.1<=A<146 : ans = 5
    elif 146<=A<159 : ans = 4
    elif 159<=A<161 :
        if B<16 or 35<=B : ans = 4
        else : ans = 3
    elif 161<=A<204 :
        if 35<=B or B<16: ans = 4
        elif 30<=B<35 or 16<=B<18.5 : ans =3
        elif 25<=B<30 or 18.5<=B<20 : ans = 2
        elif 20<=B<25: ans = 1
    elif 204<=A :
        if 20<=B<25 : ans = 1
        else : ans = 2
    else : ans = 4
    
    print(ans)