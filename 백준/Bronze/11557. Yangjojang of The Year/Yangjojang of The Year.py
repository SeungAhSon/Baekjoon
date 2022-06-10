T = int(input())

for i in range(T):
    N = int(input())
    high = 0
    school = ""
    for j in range(N):
        a, b  = input().split()
        if(int(b)>high):
            high = int(b)
            school = a
        
    print(school)