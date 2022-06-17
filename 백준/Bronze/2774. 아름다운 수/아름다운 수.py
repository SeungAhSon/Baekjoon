T = int(input())
for _ in range(T):
    digit = [0]*10
    X = input()
    
    for i in X: digit[int(i)]+=1
    print(sum(1 if int(x)!=0 else 0 for x in digit))