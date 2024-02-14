T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    if a>b: print("#{} >".format(tc))
    elif a==b: print("#{} =".format(tc))
    else : print("#{} <".format(tc))